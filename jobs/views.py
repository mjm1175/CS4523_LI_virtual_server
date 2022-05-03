from django.shortcuts import render, redirect
from .models import Job
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.

# home page
@login_required
def home(request):
	job_list = Job.objects.all()
	return render(request, 'home.html', {'jobs': job_list})

@csrf_protect
def job_post(request, slug):
	context = {}

	try:
		obj = Job.objects.get(slug=slug)
		context['job'] = obj
	except Job.DoesNotExist:
		print('couldnt find that one')

	return render(request, 'job_post.html', context)


def job_post_creation(request):
	if request.method == 'GET':
		form = CreateJobForm()
		context = {'form' : form}
		return render(request, 'job_post_creation.html', context)

	if request.method == 'POST':
		form = CreateJobForm(request.POST)

		if form.is_valid():
			obj = form.save(commit=False)
			#obj.owner = request.user
			obj.save()
			messages.success(request, 'Job post created successfully.')
			
			return redirect('job_post', slug=obj.slug)

		else:
			messages.error(request, 'Error processing your request')
			context = {'form': form}
			return render(request, 'job_post_creation.html', context)

	return render(request, 'job_post_creation.html', {})

