from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Hero
from .serializers import HeroSerializer
from rest_framework.decorators import api_view
import pyrebase

config = {
  "apiKey": "AIzaSyA5Tywq4OAYsNi5m3QHPtCNDZr4blDLO3k",
  "authDomain": "goodocity.firebaseapp.com",
  "databaseURL": "https://goodocity.firebaseio.com",
  "storageBucket": "goodocity.appspot.com",
  "projectId": "goodocity",
  "serviceAccount": "goodocity-firebase-adminsdk-79ps7-a63550c8a4.json",
  "messagingSenderId": "382652036053",
  "appId": "1:382652036053:web:e6d13708219b2cf1a4435c",
  "measurementId": "G-7JM6XVBRVD"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@api_view(['GET', 'POST', 'DELETE'])
def hero_list(request):
    if request.method == 'GET':
        heros = Hero.objects.all()
        heros_serializer = HeroSerializer(heros, many=True)
        return JsonResponse(heros_serializer.data, safe=False)
    
@api_view(['POST'])
def sign_up(request):
    print(request)

@api_view(["GET"])
def create_user(request):
    template = loader.get_template('users/index.html')
    return HttpResponse(template.render())


