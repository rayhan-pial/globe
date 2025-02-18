from django.shortcuts import render
from . models import Country
from . serializers import CountrySerializer
# Create your views here.
from rest_framework import viewsets, status

from django_filters import rest_framework as filters

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name', 'region')




