from django.urls import path
from .views import ActivityViewSet, ActivityMetricsView, ExerciseViewSet
from rest_framework.routers import DefaultRouter

# Create a router instance
router = DefaultRouter()

# Register the ActivityViewSet with the router
router.register(r'activities', ActivityViewSet, basename='activity')

# Register the ExerciseViewSet with the router
router.register(r'exercises', ExerciseViewSet, basename='exercise')

# Define urlpatterns for the app
urlpatterns = [
    # Endpoint for activity metrics (total duration, calories, distance, etc.)
    path('activities/metrics/', ActivityMetricsView.as_view({'get': 'list'}), name='activity-metrics'),
]

# Add the router's URLs to the urlpatterns
urlpatterns += router.urls
