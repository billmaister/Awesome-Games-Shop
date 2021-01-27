from django.contrib import admin
from .models import Game, GamePurchase#, AllHighScores

# Register your models here.
admin.site.register(Game)
admin.site.register(GamePurchase)