from django.shortcuts import render

from rest_framework import viewsets

from .serializers import GameDataSerializer, GameSerializer, ProfileSerializer, UserSerializer
from play_game.models import GameData
from shop.models import Game
from users.models import Profile
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from .permissions import IsAdminUserOrReadOnly, AdminReadOnly, ReadOnly

class IsDevOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        else:
            try:
                user = request.user
                userobject = Profile.objects.get(user = user)
                if userobject.is_dev:
                    return True
            except Exception:
                return False
        return False

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminReadOnly] #only admins can read user data

class GameDataViewSet(viewsets.ModelViewSet):
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer
    permission_classes = [ReadOnly] #read only permission for all

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsDevOrReadOnly]




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer #only admins can see profile data
    permission_classes = [AdminReadOnly]
