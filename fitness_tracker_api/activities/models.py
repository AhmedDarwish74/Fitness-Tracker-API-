from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import date

# Exercise model to store different types of exercises
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.name

# Custom User model extending Django's AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False, validators=[EmailValidator()])
    
    def __str__(self):
        return self.username

# Activity model to store fitness activities
class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes", validators=[MinValueValidator(1)])
    distance = models.FloatField(help_text="Distance in km", null=True, blank=True, validators=[MinValueValidator(0)])
    calories_burned = models.PositiveIntegerField(help_text="Calories burned", validators=[MinValueValidator(1)])
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.activity_type} on {self.date} by {self.user.username}"

    def save(self, *args, **kwargs):
        if self.activity_type == 'Weightlifting' and self.distance is not None:
            raise ValidationError("Distance should not be provided for Weightlifting activities.")
        if self.date > date.today():
            raise ValidationError("Activity date cannot be in the future.")
        super().save(*args, **kwargs)
