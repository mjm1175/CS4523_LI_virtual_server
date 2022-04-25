from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

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
