from django.test import TestCase
from rest_framework.test import APIClient
from .models import Exercise, Activity, User
from datetime import date

class ExerciseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.exercise = Exercise.objects.create(name="Push-ups", difficulty=5)

    def test_get_exercise(self):
        response = self.client.get(f'/api/exercises/{self.exercise.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Push-ups")
        self.assertEqual(response.data['difficulty'], 5)

    def test_create_exercise(self):
        data = {"name": "Sit-ups", "difficulty": 3}
        response = self.client.post('/api/exercises/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], "Sit-ups")
        self.assertEqual(response.data['difficulty'], 3)

    def test_update_exercise(self):
        data = {"name": "Pull-ups", "difficulty": 7}
        response = self.client.put(f'/api/exercises/{self.exercise.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Pull-ups")
        self.assertEqual(response.data['difficulty'], 7)

    def test_delete_exercise(self):
        response = self.client.delete(f'/api/exercises/{self.exercise.id}/')
        self.assertEqual(response.status_code, 204)

class ActivityAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", email="test@example.com")
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories_burned=200,
            date=date.today()
        )

    def test_get_activity(self):
        response = self.client.get(f'/api/activities/{self.activity.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['activity_type'], "Running")
        self.assertEqual(response.data['duration'], 30)

    def test_create_activity(self):
        data = {
            "user": self.user.id,
            "activity_type": "Cycling",
            "duration": 45,
            "distance": 10.0,
            "calories_burned": 300,
            "date": date.today().isoformat()
        }
        response = self.client.post('/api/activities/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['activity_type'], "Cycling")
        self.assertEqual(response.data['duration'], 45)

    def test_update_activity(self):
        data = {
            "user": self.user.id,
            "activity_type": "Weightlifting",
            "duration": 60,
            "distance": None,
            "calories_burned": 400,
            "date": date.today().isoformat()
        }
        response = self.client.put(f'/api/activities/{self.activity.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['activity_type'], "Weightlifting")
        self.assertEqual(response.data['duration'], 60)

    def test_delete_activity(self):
        response = self.client.delete(f'/api/activities/{self.activity.id}/')
        self.assertEqual(response.status_code, 204)

class ActivityMetricsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", email="test@example.com")
        Activity.objects.create(
            user=self.user,
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories_burned=200,
            date=date.today()
        )

    def test_activity_metrics(self):
        response = self.client.get('/api/activities/metrics/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("total_duration", response.data)
        self.assertIn("total_calories", response.data)
        self.assertIn("total_distance", response.data)
