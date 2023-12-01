from django.db import models
from django.contrib.auth.models import User

class GameRoom(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_game_rooms')
    players = models.ManyToManyField(User, related_name='joined_game_rooms')
    password = models.CharField(max_length=50, blank=True, null=True)
    isActive = models.BooleanField(blank=False, default=False)
    isCreatorReady = models.BooleanField(blank=False, default=False)
    isOpponentReady = models.BooleanField(blank=False, default=False)
    lastMove = models.CharField(max_length=10, blank=True, null=True)  # Replace with appropriate field type
    lastMoveUser = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
