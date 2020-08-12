from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import itemForm, registerForm

def index(request):
	context = {}
	return redirect('loginUser')

def registerUser(request):
	if request.user.is_authenticated:
		return redirect('todoView')
	else:
		form = registerForm()

		if request.method == 'POST':
			form = registerForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Account successfully created.')
				return redirect('loginUser')

		context = {'form': form}
		return render(request, 'register.html', context)

def loginUser(request):
	if request.user.is_authenticated:
			return redirect('todoView')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('todoView')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('loginUser')

@login_required(login_url='loginUser')
def todoView(request):
	if request.method == 'POST':
		form = itemForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_todo_items = TodoItem.objects.all()
			return render(request, 'todo.html', {'all_items': all_todo_items})

	else:
		all_todo_items = TodoItem.objects.all()
		return render(request, 'todo.html', {'all_items': all_todo_items})

@login_required(login_url='loginUser')
def addTodo(request):
	new_item = TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')

@login_required(login_url='loginUser')
def deleteTodo(request, todo_id):
	 item_delete = TodoItem.objects.get(id=todo_id)
	 item_delete.delete()
	 return HttpResponseRedirect('/todo/')

@login_required(login_url='loginUser')
def doneTodo(request, todo_id):
	 item_done = TodoItem.objects.get(id=todo_id)
	 item_done.done = True
	 item_done.save()
	 return HttpResponseRedirect('/todo/')

@login_required(login_url='loginUser')
def undoneTodo(request, todo_id):
	 item_done = TodoItem.objects.get(id=todo_id)
	 item_done.done = False
	 item_done.save()
	 return HttpResponseRedirect('/todo/')

@login_required(login_url='loginUser')
def updateTodo(request, todo_id):
	if request.method == 'POST':
		item = TodoItem.objects.get(id=todo_id)

		form = itemForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			all_todo_items = TodoItem.objects.all()
			return HttpResponseRedirect('/todo/')

	else:
		item = TodoItem.objects.get(id=todo_id)
		return render(request, 'update.html', {'item': item})