from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class RegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']
