from rest_framework import serializers
from .models import Exercise, User, Activity

# Serializer for the Exercise model
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

    def validate_difficulty(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Difficulty must be between 1 and 10.")
        return value

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer for the Activity model
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def validate(self, data):
        if data['activity_type'] == 'Weightlifting' and data.get('distance') is not None:
            raise serializers.ValidationError("Distance should not be provided for Weightlifting activities.")
        if data['date'] > date.today():
            raise serializers.ValidationError("Activity date cannot be in the future.")
        return data
