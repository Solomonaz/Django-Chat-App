from chat.models import Room
from django.shortcuts import render


def index_view(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'index.html', context)

def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    context = {
        'room': chat_room,
    }
    return render(request, 'room.html', context)
