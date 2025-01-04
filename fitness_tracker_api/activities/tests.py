from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Activity

class ActivityTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)  # Authenticate the user

        # Create a test activity
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories_burned=300,
            date='2023-10-01'
        )

    def test_create_activity(self):
        # Test creating a new activity
        url = reverse('activity-list')  # Make sure 'activity-list' is registered in URLs
        data = {
            'activity_type': 'Cycling',
            'duration': 45,
            'distance': 10.0,
            'calories_burned': 450,
            'date': '2023-10-02'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if created

    def test_get_activity(self):
        # Test retrieving an activity
        url = reverse('activity-detail', args=[self.activity.id])  # Make sure 'activity-detail' is registered
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if OK
        self.assertEqual(response.data['activity_type'], 'Running')  # Verify activity type

    def test_delete_activity(self):
        # Test deleting an activity
        url = reverse('activity-detail', args=[self.activity.id])  # Ensure the activity ID is passed correctly
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Check if deleted
