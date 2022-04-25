from django.shortcuts import render
from .models import Job

# Create your views here.

# home page; opens on start (eventually change to login??)
def home(request):
	job_list = Job.objects.all()
	return render(request, 'home.html', {'jobs': job_list})
