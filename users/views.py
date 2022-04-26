from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime

# Create your views here.

def register(request):
	if request.method == 'GET':
		form = RegisterForm()
		context = {'form' : form, 'register': True}
		return render(request, 'register.html', context)
	
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			print('yes')
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('home_page')
		else:
			print('no')
			print(form.errors)
			messages.error(request, 'Error processing your request')
			context = {'form': form, 'register': True}
			return render(request, 'register.html', context)

	return render(request, 'register.html', {})

@login_required
def profile(request):
	return render(request, 'profile.html', {})


@login_required
def create_resume(request):
	if request.method == 'POST':
		# request.FILES bc files upload option in form
		form = ResumeForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)

			# setting 1:1 attribute
			obj.user = request.user

			obj.save()

			messages.success(request, 'Resume created successfully.')
			return redirect('profile')
		else:
			messages.error(request, 'Error processing your request')
			context = {'form': form}
			return render(request, 'create-resume.html', context)

	if request.method == 'GET':
		form = ResumeForm()
		context = {'form': form}
		return render(request, 'create-resume.html', context)

	return render(request, 'create-resume.html', {})


class ResumeDetailView(DetailView):
	model=Resume
	template_name = 'resume-detail.html'
