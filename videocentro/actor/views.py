from django.shortcuts import render
from django.contrib.auth.forms import *
from .forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.contrib.auth import login
# Create your views here.

def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'signup.html',{'form':form})	

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())

	return render(request, 'signin.html', {'form':form})	