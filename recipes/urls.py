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