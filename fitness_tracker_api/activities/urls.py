from django.urls import path
from .views import ActivityViewSet, ActivityMetricsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')  # Register ActivityViewSet

urlpatterns = [
    path('metrics/', ActivityMetricsView.as_view({'get': 'list'}), name='activity-metrics'),  # Metrics endpoint
]

urlpatterns += router.urls  # Include router URLs