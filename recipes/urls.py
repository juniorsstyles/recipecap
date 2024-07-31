from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cakes/', views.cakes, name='cakes'),
    path('chocolate_cake/', views.chocolate_cake, name='chocolate_cake'),
    path('cheesecake/', views.cheesecake, name='cheesecake'),
    path('vanilla_cake/', views.vanilla_cake, name='vanilla_cake'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

"""
URL patterns for the recipes app.

This module defines the URL patterns for the recipes app, mapping URLs to views.

Paths:
    '' (home): The home page view.
    'cakes/' (cakes): The cakes list view.
    'chocolate_cake/' (chocolate_cake): The chocolate cake detail view.
    'cheesecake/' (cheesecake): The cheesecake detail view.
    'vanilla_cake/' (vanilla_cake): The vanilla cake detail view.
    'register/' (register): The user registration view.
    'profile/' (profile): The user profile view.
"""
