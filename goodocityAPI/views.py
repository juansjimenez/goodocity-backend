from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import psycopg2
from .models import User, Event, Community, Category
from .serializers import EventSerializer, UserSerializer, CategorySerializer, CommunitySerializer
from rest_framework.decorators import api_view
import pyrebase
from goodocity.settings import DATABASES

config = {
    "apiKey": "AIzaSyA5Tywq4OAYsNi5m3QHPtCNDZr4blDLO3k",
    "authDomain": "goodocity.firebaseapp.com",
    "databaseURL": "https://goodocity.firebaseio.com",
    "storageBucket": "goodocity.appspot.com",
    "projectId": "goodocity",
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
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        print(user_data)
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            auth.create_user_with_email_and_password(
                user_data["email"], user_data["password"])
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

    elif request.method == 'DELETE':
        count = Event.objects.all().delete()
        return JsonResponse({'message': f'{count[0]} Events were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def com_list(request):
    # Get list of all communities, create - POST - a new community
    if request.method == 'GET':
        commus = Community.objects.all()
        serializer = CommunitySerializer(commus, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        com_data = JSONParser().parse(request)
        serializer = CommunitySerializer(data=com_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, static=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Community.objects.all().delete()
        return JsonResponse({'message': f'{count[0]} Communities were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        cat_data = JSONParser().parse(request)
        serializer = CommunitySerializer(data=cat_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, static=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Category.objects.all().delete()
        return JsonResponse({'message': f'{count[0]} Categories were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


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
        event_data = JSONParser().parse(request)
        event_serializer = EventSerializer(event, data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse(event_serializer.data)
        return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def com_especific(request, id):
        try:
            community = Community.objects.get(pk=id)
        except Community.DoesNotExist:
            return JsonResponse({'message': 'The community does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CommunitySerializer(community)
            return JsonResponse(serializer.data)

        elif request.method == 'DELETE':
            community.delete()
            return JsonResponse({'message': 'Community was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            com_data = JSONParser().parse(request)
            serializer = CommunitySerializer(community, data=com_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_specific(request, id):
    try:
        user = User.objects.get(pk=id)
    except user.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=user_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def categories_communities(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    communities = Community.objects.filter(categories__id=id)
    serializer = CommunitySerializer(communities, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def categories_events(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    events = Event.objects.filter(categories__id=id)
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def events_comminties(request, id):
    try:
        community = Community.objects.get(pk=id)
    except Community.DoesNotExist:
        return JsonResponse({'message': 'The community does not exist'}, status=status.HTTP_404_NOT_FOUND)

    events = Event.objects.filter(community__id=id)
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def venue_communities(request, venue):
    communities = Community.objects.filter(venue__startswith=venue)
    serializer = CommunitySerializer(communities, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def venue_events(request, venue):
    events = Event.objects.filter(venue__startswith=venue)
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def get_participants(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get all participants of a given event
    participants = event.participants.all()
    serializer = UserSerializer(participants, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def get_members(request, id):
    try:
        community = Community.objects.get(pk=id)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'The Community does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get all members of a given community
    members = community.participants.all()
    serializer = UserSerializer(members, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["PUT"])
def add_participant(request, eid, uid):
    try:
        event = Event.objects.get(pk=eid)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        participant = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    event.participants.add(participant)
    return JsonResponse({'message': 'The participant was added correctly'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def remove_participant(request, eid, uid):
    try:
        event = Event.objects.get(pk=eid)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        participant = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    event.participants.remove(participant)
    return JsonResponse({'message': 'The participant was removed correctly'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def remove_member(request, cid, uid):
    try:
        community = Community.objects.get(pk=cid)
    except Community.DoesNotExist:
        return JsonResponse({'message': 'The community does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        member = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    community.participants.remove(member)
    return JsonResponse({'message': 'The participant was removed correctly'}, status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def add_member(request, cid, uid):
    try:
        community = Community.objects.get(pk=cid)
    except Community.DoesNotExist:
        return JsonResponse({'message': 'The community does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        member = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    community.participants.add(member)
    return JsonResponse({'message': 'The participant was added correctly'}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def sign_in(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(email=data['email'])
        serializer = UserSerializer(user)
        auth.sign_in_with_email_and_password(data['email'], data['password'])
        return JsonResponse(serializer)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)


# View only for testing sign_up feature
@api_view(["GET"])
def create_user(request):
    template = loader.get_template('users/sign_up.html')
    return HttpResponse(template.render())


@api_view(["GET"])
def sign_out(request):
    auth.current_user = None
    return JsonResponse({'message': 'Logged out succesfully'}, status=status.HTTP_204_NO_CONTENT)
