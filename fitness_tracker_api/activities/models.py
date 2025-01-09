from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import date

# Exercise model to store different types of exercises
class Exercise(models.Model):
    name = models.CharField(max_length=100)  # Name of the exercise (required)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]  # Difficulty level between 1 and 10 (required)
    )

    def __str__(self):
        return self.name  # String representation of the exercise

# Custom User model extending Django's AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False, validators=[EmailValidator()])  # Email field (required and unique)
    
    def __str__(self):
        return self.username  # String representation of the user

# Activity model to store fitness activities
class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')  # User who performed the activity (required)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)  # Type of activity (required)
    duration = models.PositiveIntegerField(help_text="Duration in minutes", validators=[MinValueValidator(1)])  # Duration in minutes (required)
    distance = models.FloatField(help_text="Distance in km", null=True, blank=True, validators=[MinValueValidator(0)])  # Distance in km (optional)
    calories_burned = models.PositiveIntegerField(help_text="Calories burned", validators=[MinValueValidator(1)])  # Calories burned (required)
    date = models.DateField(default=date.today)  # Date of the activity (default is today)

    def __str__(self):
        return f"{self.activity_type} on {self.date} by {self.user.username}"  # String representation of the activity

    def save(self, *args, **kwargs):
        # Validate that distance is not provided for Weightlifting activities
        if self.activity_type == 'Weightlifting' and self.distance is not None:
            raise ValidationError("Distance should not be provided for Weightlifting activities.")
        # Validate that the activity date is not in the future
        if self.date > date.today():
            raise ValidationError("Activity date cannot be in the future.")
        super().save(*args, **kwargs)  # Save the activity
