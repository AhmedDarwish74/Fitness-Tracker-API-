import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-default-secret-key'  # This is a default key for local development; use an environment variable in production.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to True for development mode to show detailed error messages.

# List of host/domain names that this Django site can serve.
ALLOWED_HOSTS = ['*']  # Allow requests only from localhost for local development.

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST framework for building APIs.
    'activities',  # Custom app for managing fitness activities.
]

# Middleware is a list of hooks into Django's request/response processing.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration module for the project.
ROOT_URLCONF = 'fitness_tracker_api.urls'

# Templates configuration for rendering HTML templates.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify template directories here.
        'APP_DIRS': True,  # Django will look for templates in each app's "templates" directory.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application used to serve the project.
WSGI_APPLICATION = 'fitness_tracker_api.wsgi.application'

# Database configuration for local development (using SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite for local development.
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite database file stored in the project directory.
    }
}

# Password validation settings to improve security.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CORS configuration (if using external APIs or JS)
CORS_ALLOW_ALL_ORIGINS = True  # Allow all domains; you can restrict this based on your needs.

# Internationalization settings (language and timezone).
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) settings.
STATIC_URL = '/static/'  # URL path to access static files.
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory where static files will be stored.

# Security settings for static file handling on Heroku (if deployed).
SECURE_SSL_REDIRECT = not DEBUG  # Redirect HTTP to HTTPS in production.

# Django REST framework settings for using JWT authentication.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT for authentication.
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Only authenticated users can access the API.
    ],
}

# Simple JWT token configuration for token expiration times.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Access token valid for 30 minutes.
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Refresh token valid for 1 day.
}

# Default primary key field type.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model settings (if using a custom user model in the 'activities' app).
AUTH_USER_MODEL = 'activities.User'  # Custom user model located in the 'activities' app.
