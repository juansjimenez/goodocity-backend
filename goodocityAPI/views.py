from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import psycopg2
from .models import Event, AccountManager
from .serializers import HeroSerializer
from rest_framework.decorators import api_view
import pyrebase

config = {
  "apiKey": "AIzaSyA5Tywq4OAYsNi5m3QHPtCNDZr4blDLO3k",
  "authDomain": "goodocity.firebaseapp.com",
  "databaseURL": "https://goodocity.firebaseio.com",
  "storageBucket": "goodocity.appspot.com",
  "projectId": "goodocity",
#   "serviceAccount": "goodocity-firebase-adminsdk-79ps7-a63550c8a4.json",
  "messagingSenderId": "382652036053",
  "appId": "1:382652036053:web:e6d13708219b2cf1a4435c",
  "measurementId": "G-7JM6XVBRVD"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@api_view(['GET', 'POST', 'DELETE'])
def event_list(request):
    if request.method == 'GET':
        pass

@api_view(['POST'])
def sign_up(request):
    print(request.POST.dict())
    template = loader.get_template('users/user.html')
    data = request.POST.dict()
    try:
        auth.create_user_with_email_and_password(data["email"], data["password"])
        return HttpResponse(template.render())
    except ValueError as err:
        print(err)
        return HttpResponse(template.render())
    except:
        print("There has been an error")
        return HttpResponse(template.render())

def sign_in(request):
    data = request.POST.dict()
    try:
        conn = psycopg2.connect(database="testdb", user="postgres", password="hola")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Accounts WHERE email={data['email']};")
        user = cur.fetchone()
        print(user)
        return HttpResponse()
    except:
        return HttpResponse()

# View only for testing sign_up feature
@api_view(["GET"])
def create_user(request):
    template = loader.get_template('users/sign_up.html')
    return HttpResponse(template.render())

@api_view(["GET"])
def sign_out(request):
    auth.current_user = None
    return HttpResponse()


