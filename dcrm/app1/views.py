from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def index(request):
	records = Record.objects.all()


	if request.method=='POST':
		Username=request.POST['username']

		Password=request.POST['password']

		user=authenticate(request,username=Username,password=Password)
		if user is not None:
			login(request,user)
			messages.success(request,'you have been logged in!')
			

			return redirect('index')

		else:
			messages.success(request,'There is an error logging in, Please try again...')
			return redirect('index')
	
	else:

		return render(request,'app1/home.html',{'records':records})

def logout_user(request):
	logout(request)
	messages.success(request,'You have been logged out')
	return redirect('index')

def register_user(request):
	if request.method=='POST':

		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user=authenticate(request,username=username,password=password)
			login(request, user)
			messages.success(request,'You have successfully registered')
			return redirect('index')
		else:
			messages.success(request,'Information is incorrect!')
			return render(request, 'app1/register.html',{'form':form})


	else:
		form=SignUpForm()

		return render(request, 'app1/register.html',{'form':form})

	return render(request, 'app1/register.html',{'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		customer_record = Record.objects.get(id=pk)
		return render(request, 'app1/records.html',{'customer_record':customer_record})
	else:
		messages.success(request,'You must be logged in to view this page')
		return redirect('index')

def delete_record(request,pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request,'The record has been deleted!')
		return redirect('index')
	else:
		messages.success(request,'You must be logged in to do that!')
		return redirect('index')

def add_record(request):
	form =  AddRecordForm(request.POST or None)
	if request.user.is_authenticated:

		if request.method=='POST':
			if form.is_valid():

				form.save()
				messages.success(request,'Record Added')
				return redirect('index')

		return render(request, 'app1/add_records.html',{'form':form})
	else:
		messages.success(request,'You Must be logged in')
		return redirect('index')

	# return render(request, 'app1/add_records.html',{'form':form})

def update_record(request,pk):
	if request.user.is_authenticated:
		update_record = Record.objects.get(id=pk)
		form =  AddRecordForm(request.POST or None, instance=update_record)
		if form.is_valid():
			form.save()
			messages.success(request,'Record has been updated')
			return redirect('index')
		return render(request, 'app1/update_record.html',{'form':form})

	else:
		messages.success(request,'You Must be logged in')
		return redirect('index')

		


	






