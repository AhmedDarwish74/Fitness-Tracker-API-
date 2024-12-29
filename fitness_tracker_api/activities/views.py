from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Activity
from .serializers import ActivitySerializer
from django.db.models import Sum

# ViewSet to handle CRUD operations for Activity
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['activity_type', 'date']
    ordering_fields = ['duration', 'date', 'calories_burned']

    def get_queryset(self):
        # Filter activities to show only the ones for the current user
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associate the activity with the current logged-in user
        serializer.save(user=self.request.user)

# API endpoint to view total metrics (total duration, distance, and calories burned)
@api_view(['GET'])
def activity_metrics(request):
    metrics = Activity.objects.filter(user=request.user).aggregate(
        total_duration=Sum('duration'),
        total_distance=Sum('distance'),
        total_calories=Sum('calories_burned')
    )

    return Response({
        'total_duration_minutes': metrics['total_duration'] or 0,
        'total_distance_km': metrics['total_distance'] or 0,
        'total_calories_burned': metrics['total_calories'] or 0,
    })
