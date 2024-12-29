from rest_framework import serializers
from .models import User, Activity

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Fields to include in the serializer
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(**validated_data)
        return user

# Serializer for the Activity model
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'date']  # Fields to include
        read_only_fields = ['user']  # Ensure user field is read-only

    def validate(self, data):
        # Custom validation for duration and calories burned
        if data['duration'] <= 0:
            raise serializers.ValidationError("Duration must be greater than 0.")
        if data['calories_burned'] <= 0:
            raise serializers.ValidationError("Calories burned must be greater than 0.")
        return data