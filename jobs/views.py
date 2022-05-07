from django.shortcuts import render, redirect
from .models import Job
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def search(request):
    job_search_form = SearchJobsForm()

    job_list = Job.objects.all()

    context = {}
    context['job_search_form'] = job_search_form
    context['jobs'] = job_list

    if request.method == 'POST':
        job_search_form = SearchJobsForm(request.POST)
        if job_search_form.is_valid():
            search = job_search_form.cleaned_data.get('title')
            jobs = []
            if len(search.split()) > 1:
                search_list = search.split()
                item_list = []
                for item in search_list:
                    a_list = Job.objects.filter(title__icontains=item)
                    for x in a_list:
                            item_list.append(x)
                [jobs.append(x) for x in item_list if x not in jobs]

            else:
                jobs = Job.objects.filter(title__icontains=search)

            context['jobs'] = jobs
            context['title'] = search

            # only sending jobs that fit the search
            return render(request, 'home.html', context)
    
        else:
            messages.error(request, 'Error processing your request')
            context['job_search_form'] = job_search_form
            return render(request, 'home.html', context)
    
    return None


# home page; smart search
@login_required
def home(request):
	# search
	job_search_form = SearchJobsForm()

	context = {}
	context['job_search_form'] = job_search_form

	search_request = search(request)
	if search_request is not None:
		return search_request
	# end search

	job_list = Job.objects.all()
	context['jobs'] = job_list

	return render(request, 'home.html', context)
    

@csrf_protect
def job_post(request, slug):
	# search
	job_search_form = SearchJobsForm()

	context = {}
	context['job_search_form'] = job_search_form

	search_request = search(request)
	if search_request is not None:
		return search_request
	# end search

	try:
		obj = Job.objects.get(slug=slug)
		context['job'] = obj
	except Job.DoesNotExist:
		print('couldnt find that one')

	return render(request, 'job_post.html', context)


def job_post_creation(request):
	# search
	job_search_form = SearchJobsForm()

	context = {}
	context['job_search_form'] = job_search_form

	if request.method == 'GET':
		form = CreateJobForm()
		context['form'] = form
		return render(request, 'job_post_creation.html', context)

	if request.method == 'POST':
		form = CreateJobForm(request.POST)
		search_request = search(request)

		if form.is_valid():
			obj = form.save(commit=False)
			obj.owner = request.user
			# might throw error
#			if request.user.resume: (check for this some better way)
			obj.company = request.user.resume.company
			obj.save()
			messages.success(request, 'Job post created successfully.')

			return redirect('job_post', slug=obj.slug)
		elif search_request is not None:
			return search_request
		else:
			messages.error(request, 'Error processing your request')
			context['form'] = form
			return render(request, 'job_post_creation.html', context)

	return render(request, 'job_post_creation.html', context)


def company_detail(request, slug):
    # search
    job_search_form = SearchJobsForm()

    context = {}
    context['job_search_form'] = job_search_form

    search_request = search(request)
    if search_request is not None:
        return search_request
    # end search

    obj = Company.objects.get(slug=slug)
    # getting all jobs whose company's slug matches this slug
    # (all jobs in this company)
    jobs = Job.objects.filter(company__slug=slug)

    context['company'] = obj
    context['jobs'] = jobs

    return render(request, 'company_detail.html', context)

@login_required
def company_creation(request, comp_id=None):
    # search
    job_search_form = SearchJobsForm()

    context = {}
    context['job_search_form'] = job_search_form

    if request.method == 'POST':
        search_request = search(request)

        if comp_id:
            comp = Company.objects.get(pk=comp_id)
            form = CreateCompanyForm(request.POST, request.FILES, instance=comp)
        else:
            form = CreateCompanyForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Company profile updated successfully.')

            return redirect('profile')
        elif search_request is not None:
            return search_request
        else:
            messages.error(request, 'Error processing your request')
            context['form'] = form
            return render(request, 'company_creation.html', context)    

    if request.method == 'GET':
        if comp_id:
            comp = Company.objects.get(pk=comp_id)
            form = CreateCompanyForm(instance=comp)
        else:
            form = CreateCompanyForm()
        context['form'] = form
        return render(request, 'company_creation.html', context)

    return render(request, 'company_creation.html', context)

def home_companies(request):
	# search
	job_search_form = SearchJobsForm()

	context = {}
	context['job_search_form'] = job_search_form

	search_request = search(request)
	if search_request is not None:
		return search_request
	# end search


	#	can change to filter for search
	comp_list = Company.objects.all()
	context['companies'] = comp_list
	return render(request, 'home_companies.html', context)
