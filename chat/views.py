from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Message


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:50]
    room = Message.objects.filter(room=room_name)[0:50]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages, 'room': room})


def check_messages(request, room_name):
    if request.method == 'GET':
        message_exists = Message.objects.filter(
            room=room_name).exists()
    print(message_exists)
    if message_exists:
        return HttpResponse('<div id="no-messages" class="hide-this"></div>')
    else:
        return HttpResponse('''<div id="no-messages" style="min-height: 100px; max-height: 300px; overflow-y: scroll;">
                            <p>No messages here!!</p>
                        </div>''')
