from rest_framework import serializers
from .models import Event, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', 'date_joined', 'last_login')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'venue', 'time')
