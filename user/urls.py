from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login_page,register_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
]
