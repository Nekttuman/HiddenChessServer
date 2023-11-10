from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_game_room, name="create_game_room"),
    path("list/", views.list_game_rooms, name="list_game_rooms"),
    path("join/", views.join_game_room, name="join_game_room"),
    path("move/", views.user_make_move, name="user_make_move"),
    path("check-move/", views.user_check_opponent_move, name="user_check_opponent_move"),
]