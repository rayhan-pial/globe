from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet,NeighbourCountryView

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('country/', include(router.urls)),
    path('neighbor/<str:country>', NeighbourCountryView.as_view()),

]
