from chat.models import Room, CustomUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'index.html', context)

@login_required
def room_view(request, room_name):
    user = CustomUser.objects.all()
    chat_room, created = Room.objects.get_or_create(name=room_name)
    context = {
        'room': chat_room,
        'user':user,
    }
    return render(request, 'room.html', context)
