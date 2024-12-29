from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.response import Response
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# ViewSet for the Activity model
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()  # Default queryset
    serializer_class = ActivitySerializer  # Serializer to use
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]  # Enable filtering and ordering
    filterset_fields = ['activity_type', 'date']  # Fields to filter by
    ordering_fields = ['date', 'duration', 'calories_burned']  # Fields to order by

    def get_queryset(self):
        # Only return activities for the logged-in user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the logged-in user when creating an activity
        serializer.save(user=self.request.user)

# ViewSet for activity metrics (e.g., total duration, calories burned)
class ActivityMetricsView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def list(self, request):
        # Calculate total duration, distance, and calories burned for the logged-in user
        user_activities = Activity.objects.filter(user=request.user)
        total_duration = user_activities.aggregate(Sum('duration'))['duration__sum'] or 0
        total_distance = user_activities.aggregate(Sum('distance'))['distance__sum'] or 0
        total_calories = user_activities.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

        # Return the metrics as a response
        return Response({
            'total_duration': total_duration,
            'total_distance': total_distance,
            'total_calories': total_calories,
        })