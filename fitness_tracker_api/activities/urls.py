from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, activity_metrics

# Initialize the router
router = DefaultRouter()
router.register(r'activities', ActivityViewSet)

# Define URL patterns
urlpatterns = [
    # Include all endpoints registered in the router
    path('api/', include(router.urls)),  # CRUD operations for activities

    # Custom endpoint for activity metrics
    path('api/metrics/', activity_metrics, name='activity-metrics'),  # Summary metrics
]
