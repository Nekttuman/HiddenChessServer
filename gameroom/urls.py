from django.urls import path, include
from . import views

urlpatterns = [
    path("create/", views.create_game_room, name="create_game_room"),
    path("list/", views.list_game_rooms, name="list_game_rooms"),
    path("join/", views.join_game_room, name="join_game_room"),
    path("move/", views.user_make_move, name="user_make_move"),
    path("check-move/", views.user_check_opponent_move, name="user_check_opponent_move"),
    path("user-ready-info/", views.user_ready_info, name="user_ready_info_set"),
    path("opponent-ready-check/", views.opponent_ready_check, name="opponent_ready_check"),
]