from rest_framework import serializers
from .models import Activity
from django.contrib.auth.models import User
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'activity_type', 'duration', 'distance', 'calories_burned', 'date', 'formatted_date', 'user']

    def get_formatted_date(self, obj):
        return obj.date.strftime('%d-%m-%Y')

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive number.")
        return value

    def validate_distance(self, value):
        if value <= 0:
            raise serializers.ValidationError("Distance must be a positive number.")
        return value

    def validate_calories_burned(self, value):
        if value < 0:
            raise serializers.ValidationError("Calories burned cannot be negative.")
        return value

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value
