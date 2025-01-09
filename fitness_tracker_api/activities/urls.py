from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, ActivityViewSet, ActivityMetricsView

# Create a router for the ViewSets
router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)  # Register the ExerciseViewSet
router.register(r'activities', ActivityViewSet)  # Register the ActivityViewSet

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('activity-metrics/', ActivityMetricsView.as_view({'get': 'list'}), name='activity-metrics'),  # Custom endpoint for activity metrics
]
