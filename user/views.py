from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
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
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            messages.success(request, 'Account was created for ' + user)
            login(request, account)
            return redirect('home_page')
        else:
            print('no')
            print(form.errors)
            messages.error(request, 'Error processing your request')
            context = {'form': form}
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


# not used anymore
class ResumeDetailView(DetailView):
	model=Resume
	template_name = 'resume-detail.html'

@csrf_protect
def resume_detail(request, slug):
	obj = Resume.objects.get(slug=slug)

	# get all Educations & Experiences with the same resume attached
	educations = Education.objects.filter(resume=obj)
	experiences = Experience.objects.filter(resume=obj)
	context = {}
	context['object'] = obj
	context['educations'] = educations
	context['experiences'] = experiences

	if request.method == 'POST':
		edu_form = EducationForm(request.POST)
		exp_form = ExperienceForm(request.POST)
		if edu_form.is_valid():
			o = edu_form.save(commit=False)

			o.resume = obj
			o.save()

			messages.success(request, 'Resume (education) updated successfully')
			return redirect('resume_detail', slug=slug)
		elif exp_form.is_valid():
			o = exp_form.save(commit=False)

			o.resume = obj
			o.save()

			messages.success(request, 'Resume (experience) updated successfully')
			return redirect('resume_detail', slug=slug)
		else:
			print(exp_form.errors)
			print(exp_form.skills)
			messages.error(request, 'Error processing your request')
			context['edu_form'] = edu_form
			context['exp_form'] = exp_form
			return render(request, 'resume-detail.html', context)

	if request.method == 'GET':
		edu_form = EducationForm()
		exp_form = ExperienceForm()
		context['edu_form'] = edu_form
		context['exp_form'] = exp_form
		return render(request, 'resume-detail.html', context)

	return render(request, 'resume-detail.html', context)


def home_profiles(request):
	#	can change to filter for search
	users_list = Account.objects.all()
	return render(request, 'home_profiles.html', {'users' : users_list})

@csrf_protect
def public_profile(request, slug):
    obj = Account.objects.get(slug=slug)
    context = {}
    context['object'] = obj

    return render(request, 'public_profile.html', context)

# not working/finished
def download(request, foldername, filename):
	file_path = settings.MEDIA_ROOT + '/'+foldername+'/'+filename
