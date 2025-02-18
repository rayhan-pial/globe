from django.shortcuts import render
from . models import Country
from . serializers import CountrySerializer
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from django_filters import rest_framework as filters

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name', 'region')

class NeighbourCountryView(APIView):
    def get(self, request, country):
        country = get_object_or_404(Country, name=country)
        neighbors = Country.objects.filter(region=country.region).exclude(name=country)
        serializer = CountrySerializer(neighbors, many=True)
        return Response(serializer.data)

class CountryNameView(APIView):
    def get(self, request, country):
        # country = get_object_or_404(Country, name__icontains=country)
        country = Country.objects.filter(name__icontains=country)

        # neighbors = Country.objects.filter(region=country.region).exclude(name=country)
        serializer = CountrySerializer(country,many=True)
        return Response(serializer.data)





class CountrydetailsView(APIView):
    def get(self, request):
        # countries = Country.objects.all()
        # return render(request, 'country.html', {'countries': countries})

        search_query = request.GET.get('country', '')
        if search_query:
            countries = Country.objects.filter(name__icontains=search_query)
        else:
            countries = Country.objects.all()
        return render(request, 'country.html', {'countries': countries, 'search_query': search_query})


class NeighbourCountry(APIView):
    def get(self, request, country_id):
        country = get_object_or_404(Country, id=country_id)
        neighbors = Country.objects.filter(region=country.region).exclude(name=country)
        return render(request, 'country_details.html', {'country': country, 'neighbors': neighbors})

