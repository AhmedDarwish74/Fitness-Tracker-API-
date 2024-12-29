from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    """
    Represents a fitness activity logged by a user.
    """

    RUNNING = 'Running'
    CYCLING = 'Cycling'
    WEIGHTLIFTING = 'Weightlifting'
    ACTIVITY_CHOICES = [
        (RUNNING, 'Running'),
        (CYCLING, 'Cycling'),
        (WEIGHTLIFTING, 'Weightlifting'),
    ]

    user = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    activity_type = models.CharField(
        max_length=100,
        choices=ACTIVITY_CHOICES,
        default=RUNNING,
        help_text="Type of the activity (e.g., Running, Cycling)."
    )
    duration = models.IntegerField(help_text="Duration of the activity in minutes.")
    distance = models.FloatField(help_text="Distance covered in kilometers.")
    calories_burned = models.IntegerField(help_text="Calories burned during the activity.")
    date = models.DateField(help_text="Date of the activity.")

    def __str__(self):
        return f"{self.activity_type} on {self.date} by {self.user.username}"
