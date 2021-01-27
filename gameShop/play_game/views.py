from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from shop.models import Game, GamePurchase
from .models import GameData


def save(request, game_id):
    if request.is_ajax():
        game = Game.objects.get(pk=game_id)
        data = request.GET.get('game_state')
        game_data = GameData.objects.get( user = request.user, game = game)
        game_data.save_data = data
        game_data.save()
        return JsonResponse({})
    
    return HttpResponseNotFound()
        


def load(request, game_id):
    if request.is_ajax():
        game = Game.objects.get(pk=game_id)
        game_data = GameData.objects.get( user = request.user, game = game)
        data = game_data.save_data
        if data != None:
            message = {'messageType': 'LOAD', 'gameState': data}
        else:
            message = {'messageType': 'ERROR', 'info': 'Gamestate could not be loaded.'}
        return JsonResponse(message)
    return HttpResponseNotFound()



def submit_score(request, game_id):
    if request.is_ajax():
        game = Game.objects.get(pk=game_id)
        game_data = GameData.objects.get( user = request.user, game = game)
        incoming_score = int(request.GET.get('score'))
        if incoming_score > game_data.highscore:
            game_data.highscore = incoming_score
            game_data.save()
        return JsonResponse({})
    return HttpResponseNotFound()



@login_required
def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    # Only allow the game's author and users who have bought the game to play
    if request.user != game.author and request.user.purchases.filter(game=game).count() == 0:
        return HttpResponseForbidden('You have not purchased this game yet.')

    game.times_played += 1
    game.save()

    # Create new game data if first time playing
    if not GameData.objects.filter( user = request.user, game = game).exists():
        GameData.objects.create(user = request.user, game = game)

    return render(request, 'play_game/play.html', {'game': game})
