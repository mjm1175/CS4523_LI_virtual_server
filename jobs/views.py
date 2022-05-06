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
			obj.owner = request.user
			# might throw error
			obj.company = request.user.company
			obj.save()
			messages.success(request, 'Job post created successfully.')

			return redirect('job_post', slug=obj.slug)

		else:
			messages.error(request, 'Error processing your request')
			context = {'form': form}
			return render(request, 'job_post_creation.html', context)

	return render(request, 'job_post_creation.html', {})


def company_detail(request, slug):
    obj = Company.objects.get(slug=slug)
    # getting all jobs whose company's slug matches this slug
    # (all jobs in this company)
    jobs = Job.objects.filter(company__slug=slug)

    context = {}
    context['company'] = obj
    context['jobs'] = jobs

    return render(request, 'company_detail.html', context)


def company_creation(request):
	if request.method == 'GET':
		form = CreateCompanyForm()
		context = {'form' : form}
		return render(request, 'company_creation.html', context)

	if request.method == 'POST':
		form = CreateCompanyForm(request.POST)

		if form.is_valid():
			obj = form.save()
			messages.success(request, 'Successfully added new company.')

			return redirect('home_page')

		else:
			messages.error(request, 'Error processing your request')
			context = {'form': form}
			return render(request, 'company_creation.html', context)

	return render(request, 'company_creation.html', {})

def home_companies(request):
	#	can change to filter for search
	comp_list = Company.objects.all()
	return render(request, 'home_companies.html', {'companies' : comp_list})
