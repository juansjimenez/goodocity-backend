from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Hero
from .serializers import HeroSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def hero_list(request):
    if request.method == 'GET':
        heros = Hero.objects.all()
        heros_serializer = HeroSerializer(heros, many=True)
        return JsonResponse(heros_serializer.data, safe=False)
    

@api_view(['GET', 'POST', 'DELETE'])
def hero_list(request):
    if request.method == 'GET':
        heros = Hero.objects.all()
        heros_serializer = HeroSerializer(heros, many=True)
        return JsonResponse(heros_serializer.data, safe=False)
