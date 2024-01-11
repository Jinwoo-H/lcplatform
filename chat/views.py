from django.shortcuts import render, redirect
from .models import Discussion, Chat
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        discussion_questions = Discussion.objects.all().order_by('-created_at')
        return render(request, 'discussions.html', {'discussion_questions': discussion_questions})
    else:
        messages.success(request, "Not Logged In")
        return redirect('home')

def room(request, room_name):
    if request.user.is_authenticated:
        question = Discussion.objects.get(id=room_name)
        username = request.user.username
        # get last 20 messages
        chats = reversed(Chat.objects.filter(room=room_name).order_by('-timestamp')[:20])

        return render(request, "room.html", {"room_name": room_name, "question": question, "username": username, "chats": chats})
    else:
        messages.success(request, "Not Logged In")
        return redirect('home')
    
def add_discussion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            link = request.POST.get('link')
            details = request.POST.get('details')
            form_instance = Discussion(discussion_question=title, discussion_link=link, discussion_details=details, belongs_to=request.user.username)
            form_instance.save()
            messages.success(request, 'Discussion Posted')
            return redirect('index')
        return render(request, "add_discussion.html", {})
    else:
        messages.success(request, "Not Logged In")
        return redirect('home')