from rest_framework import serializers
from .models import Exercise, Activity
from datetime import date

# Serializer for the Exercise model
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'  # Include all fields from the Exercise model

    def validate_difficulty(self, value):
        # Validate that the difficulty is between 1 and 10
        if value < 1 or value > 10:
            raise serializers.ValidationError("Difficulty must be between 1 and 10.")
        return value

# Serializer for the Activity model
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'  # Include all fields from the Activity model

    def validate(self, data):
        # Validate that distance is not provided for Weightlifting activities
        if data['activity_type'] == 'Weightlifting' and data.get('distance') is not None:
            raise serializers.ValidationError("Distance should not be provided for Weightlifting activities.")
        # Validate that the activity date is not in the future
        if data['date'] > date.today():
            raise serializers.ValidationError("Activity date cannot be in the future.")
        return data
