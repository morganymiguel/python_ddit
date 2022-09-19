from django.shortcuts import render

def index(request): 
    return render(request, 'chat/index.html')
# Create your views here.
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
def tetris(request, room_name):
    return render(request, "chat/tetris_network.html", {"room_name": room_name})
def room_tetris(request, room_name):
    return render(request, "chat/room_tetris.html", {"room_name": room_name})
