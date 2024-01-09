from django.shortcuts import render, redirect
from .models import Discussion
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        discussion_questions = Discussion.objects.all()
        return render(request, 'discussions.html', {'discussion_questions': discussion_questions})
    else:
        messages.success(request, "Not Logged In")
        return redirect('home')

def room(request, room_name):
    if request.user.is_authenticated:
        question = Discussion.objects.get(id=room_name)
        username = request.user.username
        return render(request, "room.html", {"room_name": room_name, "question": question, "username": username})
    else:
        messages.success(request, "Not Logged In")
        return redirect('home')