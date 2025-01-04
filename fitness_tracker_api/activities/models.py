from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from datetime import date

# Custom User model extending Django's AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    username = models.CharField(max_length=30, unique=True)  # Ensure username is unique
    password = models.CharField(max_length=128)  # Password field

    def __str__(self):
        return self.username  # String representation of the User model

# Activity model to store fitness activities
class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
    ]  # Predefined choices for activity types
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')  # Link activity to a user
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)  # Type of activity
    duration = models.PositiveIntegerField(help_text="Duration in minutes", validators=[MinValueValidator(1)])  # Duration of the activity
    distance = models.FloatField(help_text="Distance in km", null=True, blank=True)  # Distance covered (optional)
    calories_burned = models.PositiveIntegerField(help_text="Calories burned")  # Calories burned
    date = models.DateField(default=date.today)  # Date of the activity

    def __str__(self):
        return f"{self.activity_type} on {self.date} by {self.user.username}"  # String representation of the Activity model

    def save(self, *args, **kwargs):
        # Custom validation to ensure distance is not provided for Weightlifting activities
        if self.activity_type == 'Weightlifting' and self.distance is not None:
            raise ValueError("Distance should not be provided for Weightlifting activities.")
        super().save(*args, **kwargs)  # Call the parent class's save method

