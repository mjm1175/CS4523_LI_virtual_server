from django.shortcuts import render, redirect
from .models import Job
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import FileResponse

# Create your views here.

def search(request):
    job_search_form = SearchJobsForm()

    job_list = Job.objects.all()

    context = {}
    context['job_search_form'] = job_search_form
    context['jobs'] = job_list

    if request.method == 'POST':
        job_search_form = SearchJobsForm(request.POST)
        context['job_search_form'] = job_search_form

        if job_search_form.is_valid():
            # might need to check if not None  

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

            category = job_search_form.cleaned_data.get('category')
            location = job_search_form.cleaned_data.get('location')

            if category is not None and category != '' and category != 'N/A':
                jobs = jobs.filter(category=category)
            if location is not None and location != '' and location != 'N/A':
                jobs = jobs.filter(state=location)

            context['jobs'] = jobs
            context['title'] = search

            # only sending jobs that fit the search
            return render(request, 'home.html', context)
    
    return None

from user.views import is_email_verified

# home page; smart search

@login_required()
def home(request):
	if not request.user.email_confirmed:
		return redirect('verify_email')
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

	context = {}

	try:
		obj = Job.objects.get(slug=slug)
		context['job'] = obj
	except Job.DoesNotExist:
		print('couldnt find that one')

	return render(request, 'job_post.html', context)


def job_post_creation(request, job_id=None):

    context = {}

    if request.method == 'GET':
        if job_id:
            job = Job.objects.get(pk=job_id)
            form = CreateJobForm(instance=job)
        else:
            form = CreateJobForm()

        context['form'] = form
        return render(request, 'job_post_creation.html', context)

    if request.method == 'POST':
        if job_id:
            job = Job.objects.get(pk=job_id)
            form = CreateJobForm(request.POST, instance=job)
        else:
            form = CreateJobForm(request.POST)


        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            # might throw error
    #			if request.user.resume: (check for this some better way)
            obj.company = request.user.resume.company
            obj.save()
            messages.success(request, 'Job post created successfully.')

            return redirect('job_post', slug=obj.slug)
        else:
            messages.error(request, 'Error processing your request')
            context['form'] = form
            return render(request, 'job_post_creation.html', context)

    return render(request, 'job_post_creation.html', context)

def company_detail(request, slug):

    context = {}

    obj = Company.objects.get(slug=slug)
    # getting all jobs whose company's slug matches this slug
    # (all jobs in this company)
    jobs = Job.objects.filter(company__slug=slug)

    context['company'] = obj
    context['jobs'] = jobs

    return render(request, 'company_detail.html', context)

@login_required
@user_passes_test(is_email_verified, 'verify_email', None)
def company_creation(request, comp_id=None):

    context = {}

    if request.method == 'POST':

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

@login_required
@user_passes_test(is_email_verified, 'verify_email', None)
def home_companies(request):

	context = {}

	#	can change to filter for search
	comp_list = Company.objects.all()
	context['companies'] = comp_list
	return render(request, 'home_companies.html', context)


def apply(request, slug, app_id=None):
    job = Job.objects.get(slug=slug)
    context = {}
    context['job'] = job

    if request.method == 'POST':
        if app_id:
            app = Application.objects.get(pk=app_id)
            form = ApplicationForm(request.POST, request.FILES, instance=app)
        else:
            form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)

            # setting foreign keys
            obj.applicant = request.user
            obj.job = job

            # setting upload fields
            # could also check for if upload_resume is None
            # if this works we can change upload_resume to be resume
            if form.cleaned_data.get('use_profile_resume') == 'Yes':
                obj.resume = request.user.resume.cv
            
            if form.cleaned_data.get('use_profile_cover_letter') == 'Yes':
                obj.cover_letter = request.user.resume.cover_letter

            obj.save()
            messages.success(request, 'Application submitted successfully.')

            return redirect('home_page')

        else:
            messages.error(request, 'Error processing your request')
            context['form'] = form
            return render(request, 'job_application.html', context)    

    if request.method == 'GET':
        if app_id:
            app = Application.objects.get(pk=app_id)
            form = ApplicationForm(instance=app)
        else:
            form = ApplicationForm()

        context['form'] = form
        return render(request, 'job_application.html', context)

    return render(request, 'job_application.html', context)


def view_applications(request, slug):
    # passing slug of the job posting
    job = Job.objects.get(slug=slug)
    apps = Application.objects.filter(job=job)

    context = {}
    context['job'] = job
    context['apps'] = apps

    return render(request, 'view_applications.html', context)

def delete_job(request, pk):
    job = Job.objects.get(pk=pk)  

    if request.method == 'POST':        
        job.delete()                   
        messages.success(request, 'Job post deleted successfully')
        return redirect('profile')            

    return render(request, 'view_applications.html', {'job': job})

def download_from_application(request, id, attrib_name):
    obj = Application.objects.get(pk=id)
    if attrib_name == 'cover_letter':
        filename = obj.cover_letter.path
    elif attrib_name == 'resume':
        filename = obj.resume.path
    response = FileResponse(open(filename, 'rb'))
    return response 


def delete_application(request, pk):
    app = Application.objects.get(pk=pk)  

    if request.method == 'POST':        
        app.delete()                   
        messages.success(request, 'Application deleted successfully')
        return redirect('profile')            

    return render(request, 'my_applications.html', {'app': app})


@login_required
@user_passes_test(is_email_verified, 'verify_email', None)
def my_applications(request):
    apps = Application.objects.filter(applicant=request.user)

    context = {}
    context['apps'] = apps

    return render(request, 'my_applications.html', context)    
