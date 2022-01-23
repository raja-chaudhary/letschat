from django.shortcuts import render

# Create your views here.
from .models import Message


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:50]
    room = Message.objects.filter(room=room_name)[0:50]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages, 'room': room})