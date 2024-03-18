from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Item, Match
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'image','userImage','user', 'location' ,'rating' ,'title', 'item' ,'size' ,'brand' ,'description', 'show', 'price')

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('item1', 'item2')
