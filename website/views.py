from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Question, Topic
from .forms import AddQuestionForm, SignUpForm
from django.http import JsonResponse

# Create your views here.
def home(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Logged In")
			return redirect('home')
		else:
			messages.success(request, "Username or Password Incorrect")
			return redirect('home')
	else:
		questions = Question.objects.filter(belongs_to=request.user.username).order_by('-created_at')
		# topics_list = list(questions.topics.split(","))
		return render(request, 'home.html', {'questions': questions})
	
def logout_user(request):
	logout(request)
	messages.success(request, "Logged Out")
	return redirect('home')

def details(request, pk):
	if request.user.is_authenticated:
		details = Question.objects.get(id=pk)
		return render(request, 'details.html', {'details': details})
	else:
		messages.success(request, 'Not Logged In')
		return redirect('home')

def add_question(request):
	form = AddQuestionForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				
				#Take topics and put into list
				topics_list = request.POST.get('topics').split(",")
				difficulty = request.POST.get('difficulty')
				code = request.POST.get('code')
				
				#Get existing topics in Topic model into a list
				existingTopics = Topic.objects.filter(belongs_to=request.user.username).values_list('topic_name', flat=True)

				#Once submitting form, Topics model will update with new topics by checking existing topics with form data
				for topic1 in topics_list:
					if topic1 not in existingTopics:
						topic_instance = Topic(topic_name=topic1, belongs_to=request.user.username)
						topic_instance.save()

				add_question = form.save(commit=False)

				model_insance = Question(favorite=add_question.favorite, question_name=add_question.question_name, link=add_question.link, notes=add_question.notes, topics=topics_list, difficulty=difficulty, belongs_to=request.user.username, code=code)
				model_insance.save()
				messages.success(request, 'Question Added')
				return redirect('home')
		return render(request, 'add_question.html', {'form':form})
	else:
		messages.success(request, "Not Logged In")
		return redirect('home')
	
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Successfully Registered!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': form})

def filter_entires(request):
	selected_filter = request.GET.get('selected_filter')
	filter_entires = Question.objects.filter(difficulty=selected_filter).values()
	return JsonResponse(list(filter_entires), safe=False)

def update_question(request, pk):
	current_question = Question.objects.get(id=pk)
	if request.user.is_authenticated and current_question.belongs_to == request.user.username:
		model_insance = get_object_or_404(Question, id=pk)
		topics = model_insance.topics
		topics_string = ','.join(map(str, topics))
		code = model_insance.code

		form = AddQuestionForm(request.POST or None, instance=current_question)
		if form.is_valid():
			
			form_instance = form.save(commit=False)
			form_instance.topics = request.POST.get('topics').split(",")
			form.instance.difficulty = request.POST.get('difficulty')
			form.instance.code = request.POST.get('code')
			form_instance.save()
			messages.success(request, "Question has been updated")
			return redirect('home')
		return render(request, 'update_question.html', {'form': form, 'topics': topics_string, 'question': current_question, 'code': code})
	else:
		messages.success(request, 'Not Logged In')
		return redirect('home')
		
def remove_question(request, pk):
	delete_it = Question.objects.get(id=pk)
	if request.user.is_authenticated and delete_it.belongs_to == request.user.username:
		delete_it.delete()
		messages.success(request, "Deleted Question")
		return redirect('home')
	else:
		messages.success(request, "Could Not Delete Question")
		return redirect('home')