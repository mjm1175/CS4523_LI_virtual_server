from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from datetime import datetime
import requests
import math

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
	usr = request.user

	context = {}
	context['object'] = request.user

	try:
		if usr.resume:
			educations = Education.objects.filter(resume=usr.resume)
			experiences = Experience.objects.filter(resume=usr.resume)
			context['educations'] = educations
			context['experiences'] = experiences
	except Account.resume.RelatedObjectDoesNotExist:
		context = {}

	return render(request, 'profile.html', context)


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

	try:
		if obj.resume:
			educations = Education.objects.filter(resume=obj.resume)
			experiences = Experience.objects.filter(resume=obj.resume)

			context['educations'] = educations
			context['experiences'] = experiences    
	except Account.resume.RelatedObjectDoesNotExist:
		context = {}


	context['object'] = obj

	return render(request, 'public_profile.html', context)


# not working/finished
def download(request, foldername, filename):
	file_path = settings.MEDIA_ROOT + '/'+foldername+'/'+filename

def base64_encode(message):
        import base64
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

@csrf_protect
def zoom_callback(request):
    code = request.POST.get("code", False)
    data = requests.post(f"https://zoom.us/oauth/token?grant_type=authorization_code&code={code}&redirect_uri=http://159.203.182.153:8000/zoom/callback/", headers={
        "Authorization": "Basic " + base64_encode("dh0v4C7XRJyO5CJDJs5yaw:olo5d6l6VRQmo7FKd9v3z7DRHk8YiH7L")
                                                })
    #print(data.text)
    request.session["zoom_access_token"] = data.json()["access_token"]

    return HttpResponseRedirect("/meetingCreation/")

@csrf_protect
def schedule_interview(request):
    if request.method == "POST":
        data = requests.post("https://api.zoom.us/v2/users/me/meetings", headers={                                                   'content-type': "application/json",
              "authorization": f"Bearer {request.session['zoom_access_token']}"                                                          }, data = json.dumps({                                  
                  "topic": f"LinkedIncognito Candidate Interview",                                                                         "type": 2, "start_time": request.POST["time"],                                                                                
                  }))
        #print(data.json()["join_url"], data.json()["start_url"])
        # ChatMessage(from_id=request.user.id, to_id=candidate.id, application_id=app.id, 
        #   message=f"Hello! Your interview been successfully created! Please join this 
        #   <a href='{data.json()['join_url']}'>Zoom meeting</a> on {data.json()['start_time']} UTC. Good Luck!").save()
        # ChatMessage(from_id=request.user.id, to_id=candidate.id, application_id=app.id, 
        # message=f"This is only viewable to you, to start the Zoom meeting, click this 
        # <a href='{data.json()['start_url']}'>link</a>.", public=False).save()

        return HttpResponseRedirect(f"/meetingCreation/")

    else:
                                                                                                                                return render(request, "meetingCreation.html")

