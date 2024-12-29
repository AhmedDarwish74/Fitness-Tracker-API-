from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, activity_metrics

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, ActivityMetricsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router for the ActivityViewSet
router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),  # Include all ActivityViewSet URLs
    path('metrics/', ActivityMetricsView.as_view({'get': 'list'}), name='activity-metrics'),  # Metrics endpoint
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh endpoint
]