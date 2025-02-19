from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet,NeighbourCountryView,CountryNameView,CountrydetailsView, NeighbourCountry

router = DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('country/', include(router.urls)),
    path('neighbor/<str:country>', NeighbourCountryView.as_view()),
    path('country-name/<str:country>', CountryNameView.as_view()),

    path('all-country/', CountrydetailsView.as_view(),name='country_list'),

    path('countries/<int:country_id>/', NeighbourCountry.as_view(), name='country_details'),

]
