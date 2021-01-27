from rest_framework import serializers
from play_game.models import GameData
from shop.models import Game
from users.models import Profile
from django.contrib.auth.models import User

class GameDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameData
        fields = ('game','id','highscore','save_data')

class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ('name', 'description', 'price', 'source', 'times_played')

    #create function added to POST new games through API user field and times_played filled automaticly

    def create(self, validated_data, **kwargs):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        validated_data['author'] = user
        validated_data['times_played'] = 0
        return Game.objects.create(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'is_dev')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
