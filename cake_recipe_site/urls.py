from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in authentication URLs
]

"""
Main URL configuration for the Django project.

This module defines the main URL patterns for the Django project, 
including admin, app-specific, and authentication URLs.

Paths:
    'admin/' (admin.site.urls): The Django admin interface.
    '' (include('recipes.urls')): The URLs for the recipes app.
    'accounts/' (include('django.contrib.auth.urls')): The built-in authentication URLs provided by Django.
"""
