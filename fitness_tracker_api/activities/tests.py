from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Activity

class ActivityMetricsTests(APITestCase):
    def setUp(self):
        # Create a default user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create some activities for the user
        Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration=30,
            distance=5.0,
            calories_burned=300,
            date='2024-12-22'
        )
        Activity.objects.create(
            user=self.user,
            activity_type='cycling',
            duration=45,
            distance=10.0,
            calories_burned=400,
            date='2024-12-21'
        )

    def test_activity_metrics(self):
        # Log in
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the metrics endpoint
        response = self.client.get('/api/metrics/')

        # Check the API response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data in the response
        self.assertEqual(response.data['total_duration'], 75)  # 30 + 45
        self.assertEqual(response.data['total_distance'], 15.0)  # 5.0 + 10.0
        self.assertEqual(response.data['total_calories'], 700)  # 300 + 400

    def test_activity_metrics_no_activities(self):
        # Create another user with no activities
        another_user = User.objects.create_user(username='anotheruser', password='password')

        # Log in as the second user
        self.client.login(username='anotheruser', password='password')

        # Send a GET request to the metrics endpoint
        response = self.client.get('/api/metrics/')

        # Check the API response for user with no activities
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure that the metrics are zero
        self.assertEqual(response.data['total_duration'], 0)
        self.assertEqual(response.data['total_distance'], 0)
        self.assertEqual(response.data['total_calories'], 0)
