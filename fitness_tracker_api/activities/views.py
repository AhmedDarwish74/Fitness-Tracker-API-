from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Exercise, Activity
from .serializers import ExerciseSerializer, ActivitySerializer

# ViewSet for the Exercise model
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()  # Retrieve all exercises
    serializer_class = ExerciseSerializer  # Use the ExerciseSerializer

# ViewSet for the Activity model
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()  # Retrieve all activities
    serializer_class = ActivitySerializer  # Use the ActivitySerializer

# Custom ViewSet for Activity Metrics
class ActivityMetricsView(viewsets.ViewSet):
    def list(self, request):
        try:
            # Calculate total duration, calories burned, and distance
            total_duration = sum(activity.duration for activity in Activity.objects.all())
            total_calories = sum(activity.calories_burned for activity in Activity.objects.all())
            total_distance = sum(activity.distance for activity in Activity.objects.all() if activity.distance is not None)

            # Prepare the response data
            metrics = {
                "total_duration": total_duration,
                "total_calories": total_calories,
                "total_distance": total_distance,
            }
            return Response(metrics, status=status.HTTP_200_OK)  # Return the metrics
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Handle any exceptions
