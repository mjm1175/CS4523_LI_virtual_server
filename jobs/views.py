from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.

# home page
@login_required
def home(request):
	job_list = Job.objects.all()
	return render(request, 'home.html', {'jobs': job_list})

@csrf_protect
def job_post(request, slug):
    obj = Jobs.objects.get(slug=slug)

    context = {}
    context['job'] = obj  

    return render(request, 'job_post.html', context)
