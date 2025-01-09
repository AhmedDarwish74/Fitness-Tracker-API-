"""
URL configuration for fitness_tracker_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    # Path for the home page (root)
    path('', lambda request: HttpResponse('<h1>Welcome to Fitness Tracker API!</h1><p>Use /api/ for API access.</p>'), name='home'),
    
    # Path for Django admin panel
    path('admin/', admin.site.urls),

    # Include the app-level URLs (activities)
    path('api/', include('activities.urls')),  # Assuming 'activities' is the name of your app
]
