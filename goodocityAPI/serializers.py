from rest_framework import serializers

from .models import Hero


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class User:
        model = User
        fields = ('name', 'address', 'email', 'password')