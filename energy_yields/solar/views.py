from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .serializers import SolarYieldSerializer
from .models import SolarYield


class SolarYieldList(generics.ListAPIView):
    queryset = SolarYield.objects.filter(country="de")
    serializer_class = SolarYieldSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state']

class LoadFixture(View):
    def get(self, request):
        return HttpResponse("loaded some fixture")