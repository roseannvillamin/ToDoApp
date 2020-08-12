from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TodoItem

class itemForm(forms.ModelForm):
	class Meta:
		model = TodoItem
		fields = ["content", "done"]

class registerForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]