from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import psycopg2
from .models import User, Event, AccountManager
from .serializers import EventSerializer, UserSerializer
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
def user_list(request):
    # Get list of all users, create - POST - a new user, DELETE all users.
    if request.method == 'GET':
        events = User.objects.all()
        serializer = UserSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        event_data = JSONParser().parse(request)
        serializer = UserSerializer(data=event_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def event_list(request):
    # Get list of all events, create - POST - a new event, DELETE all events.
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        event_data = JSONParser().parse(request)
        serializer = EventSerializer(data=event_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        count = Event.objects.all().delete()
        return JsonResponse({'message': '{} Events were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def event_specific(request, id):
    # Generate requests for a specific event by id.
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        event.delete()
        return JsonResponse({'message': 'Event was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)  
    
    elif request.method == 'PUT':
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
