from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('country/', include(router.urls)),
]
