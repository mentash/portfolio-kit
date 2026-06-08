# apps/core/urls.py

from django.urls import path, reverse
from . import views

app_name = 'core'

urlpatterns = [
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
]

