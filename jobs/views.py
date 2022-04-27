from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.

# home page
@login_required
def home(request):
	job_list = Job.objects.all()
	return render(request, 'home.html', {'jobs': job_list})
