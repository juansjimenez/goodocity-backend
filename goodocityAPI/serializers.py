from rest_framework import serializers
from .models import Event, User, Community, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name',
                  'username', 'date_joined', 'last_login', 'picture')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'venue',
                  'time', 'participants', 'categories', 'community', 'picture')


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'name', 'description',
                  'venue', 'participants', 'categories', 'picture')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
