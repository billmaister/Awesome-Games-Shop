from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField()
    source = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    times_played = models.PositiveIntegerField(default=0)

    def get_times_sold(self):
        return GamePurchase.objects.filter(game=self).count()

    def __str__(self):
        return self.name

    # Needed for redirect after adding new game
    def get_absolute_url(self):
        return reverse('game-detail', kwargs={'pk': self.pk})


    # TODO: Make fields visible on admin page


class GamePurchase(models.Model):
    # In order to prevent reuse of payments, don't cascade on delete to retain payment info 
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='purchases')
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL, related_name='purchases')
    purchase_date = models.DateTimeField(default=timezone.now)
    purchase_price = models.PositiveSmallIntegerField()
    purchase_id = models.CharField(max_length=64, unique=True)
    purchase_ref = models.CharField(max_length=64, unique=True)

    def __str__(self):
        username = self.user.username if self.user != None else "USER_UNDEFINED"
        game_name = self.game.name if self.game != None else "DELETED_GAME"
        return game_name + " by, " + username