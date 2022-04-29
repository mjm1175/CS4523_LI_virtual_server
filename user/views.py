from django.shortcuts import render
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from datetime import datetime


# Create your views here.
def register(request):
	if request.method == 'GET':
		form = RegisterForm()
		context = {'form' : form}
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
			context = {'form': form}
			return render(request, 'register.html', context)

	return render(request, 'register.html', {})
