from django.shortcuts import render
from .models import Room

def todo_list(request):
    room = Room.objects.all()
    return render(request, "todos/todo_list.html", {"room": room})
