# gameroom/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameRoom
from django.http import JsonResponse


@login_required
def create_game_room(request):
    if request.method == "POST":
        roomName = request.POST["room-name"]
        roomPswd = request.POST["room-password"]

        gameroom = GameRoom(name=roomName, creator=request.user,
                            password=roomPswd, isActive=True)
        gameroom.save()
        gameroom.players.add(request.user)

        return JsonResponse({'message': 'Room created', 'room-id': str(gameroom.id)})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)


@login_required
def list_game_rooms(request):
    if request.method == "POST":
        rooms = {}
        gamerooms = GameRoom.objects.all()
        for room in gamerooms:
            if len(room.players.all()) < 2:
                rooms[room.id] = {"room-name": room.name, "isOpen": room.password == ""}
                print(room.id, len(room.players.all()), room.name, room.password)

        return JsonResponse({'message': 'Rooms list', 'rooms': rooms})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)


@login_required
def join_game_room(request):
    if request.method == "POST":
        roomId = request.POST["room-id"]
        roomPswd = request.POST["room-password"]

        room = GameRoom.objects.filter(id=roomId).first()

        if room == None:
            return JsonResponse({'message': 'wrong room id'})
        if room.password != roomPswd:
            return JsonResponse({'message': 'wrong room password'})
        if len(room.players.all()) > 1:
            return JsonResponse({'message': 'room already full'})

        room.players.add(request.user)
        print(roomId)
        return JsonResponse({'message': 'Successfully joined', 'room-id': roomId})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)


@login_required
def user_make_move(request):
    if request.method == "POST":
        roomId = request.POST["room-id"]
        prevX = request.POST["prev-pos-x"]
        prevY = request.POST["prev-pos-y"]
        nextX = request.POST["next-pos-x"]
        nextY = request.POST["next-pos-y"]

        room = GameRoom.objects.filter(id=roomId).first()

        room.lastMove = prevX + prevY + nextX + nextY
        room.lastMoveUser = request.user
        print(room.lastMoveUser.id)

        print(roomId, prevX, prevY, nextX, nextY, room.lastMove)
        room.save()

        return JsonResponse({'message': 'Successfully moved', 'room-id': roomId})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)


@login_required
def user_check_opponent_move(request):
    if request.method == "POST":
        roomId = request.POST["room-id"]

        room = GameRoom.objects.filter(id=roomId).first()
        print(room.lastMoveUser)

        if not room.lastMoveUser:
            return JsonResponse({'message': 'no new moves'})
        elif room.lastMoveUser.id != request.user.id:
            move = str(room.lastMove)
            print(move)
            return JsonResponse(
                {'message': 'new move', 'prev-pos-x': move[0], 'prev-pos-y': move[1], 'next-pos-x': move[2],
                 'next-pos-y': move[3]})
        else:
            return JsonResponse({'message': 'no new moves'})

    else:
        return JsonResponse({'message': 'invalid request'}, status=400)
