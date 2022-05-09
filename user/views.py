from django.shortcuts import render, redirect
from django.contrib import messages
from jobs.views import search
from jobs.forms import SearchJobsForm
from jobs.models import Job
from .forms import *
from .models import *
from .functions import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse, Http404, FileResponse
from django.http.response import JsonResponse
from django.conf import settings
import os
import jwt
import requests
import json
from time import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def project_upload(request):
    if request.method == 'GET':
        form = ProjectImplicitForm()
        model = ProjectImplicit.objects.all()
        context = {
            'form': form,
            'model': model
        }
        return render(request, 'test.html', context)
    if request.method == 'POST':
        form = ProjectImplicitForm(request.POST)
        uploaded_file = request.FILES['implicit']
        print(uploaded_file.name)
        print(uploaded_file.size)
        implicit = ProjectImplicit(
            user=request.user,
            project_implicit=uploaded_file
        )
        implicit.save()
        print(implicit.project_implicit.name)
        return redirect('profile')
# Create your views here.
# helper func to check if email verification 
def is_email_verified(user):
    return user.email_confirmed


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form' : form}
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            obj = form.save()

            # send validation email
            to_email = form.cleaned_data.get('email')
            welcome = WelcomeEmail(obj.uniqueId)
            e_mail = welcome.email()
            print(obj.uniqueId)
            send_email(e_mail, welcome.subject, [to_email])

            user = form.cleaned_data.get('username')
            # i think this part is the auto login
            #email = form.cleaned_data.get('email')
            #raw_password = form.cleaned_data.get('password1')
            #account = authenticate(email=email, password=raw_password)
            messages.success(request, 'Account was created for ' + user)
            #login(request, account)
            return redirect('verify_email')
        else:
            messages.error(request, 'Error processing your request')
            context = {'form': form}
            return render(request, 'register.html', context)

@login_required
@user_passes_test(is_email_verified, 'verify_email', None)
def profile(request):
	# search
	job_search_form = SearchJobsForm()
	model = ProjectImplicit.objects.all()
	context = {}
	context['job_search_form'] = job_search_form
	context['model'] = model
	search_request = search(request)
	if search_request is not None:
		return search_request
	else:
		print("getting none")
        # end search

	usr = request.user

	context['object'] = request.user

	try:
		if usr.resume:
			educations = Education.objects.filter(resume=usr.resume)
			experiences = Experience.objects.filter(resume=usr.resume)
			context['educations'] = educations
			context['experiences'] = experiences
	except Account.resume.RelatedObjectDoesNotExist:
		pass

	return render(request, 'profile.html', context)


@login_required
@user_passes_test(is_email_verified, 'verify_email', None)
def create_resume(request, res_id=None):
    # search
    job_search_form = SearchJobsForm()

    context = {}
    context['job_search_form'] = job_search_form

    if request.method == 'POST':
        search_request = search(request)

        if res_id:
            res = Resume.objects.get(pk=res_id)
            form = ResumeForm(request.POST, request.FILES, instance=res)
        else:
            # request.FILES bc files upload option in form
            form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)

            # setting 1:1 attribute
            obj.user = request.user
            obj.last_updated = datetime.now

            obj.save()

            messages.success(request, 'Resume created successfully.')
            return redirect('profile')
        elif search_request is not None:
            return search_request
        else:
            messages.error(request, 'Error processing your request')
            context['form'] = form
            if request.user.role == "Employer":
                return render(request, 'create-resume-employer.html', context)
            else:
                return render(request, 'create-resume.html', context)

    if request.method == 'GET':
        if res_id:
            res = Resume.objects.get(pk=res_id)
            form = ResumeForm(instance=res)
        else:
            form = ResumeForm()
        context['form'] = form
        if request.user.role == "Employer":
            return render(request, 'create-resume-employer.html', context)
        else:
            return render(request, 'create-resume.html', context)

    if request.user.role == "Employer":
        return render(request, 'create-resume-employer.html', context)
    else:
        return render(request, 'create-resume.html', context)


# not used anymore
class ResumeDetailView(DetailView):
	model=Resume
	template_name = 'resume-detail.html'

@csrf_protect
def resume_detail(request, slug):
	# search
	job_search_form = SearchJobsForm()

	context = {}
	context['job_search_form'] = job_search_form
	obj = Resume.objects.get(slug=slug)

	# get all Educations & Experiences with the same resume attached
	educations = Education.objects.filter(resume=obj)
	experiences = Experience.objects.filter(resume=obj)
	context['object'] = obj
	context['educations'] = educations
	context['experiences'] = experiences

	if request.method == 'POST':
		search_request = search(request)

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
		elif search_request is not None:
			return search_request
		else:
			print(exp_form.errors)
			print(exp_form.skills)
			messages.error(request, 'Error processing your request')
			context['edu_form'] = edu_form
			context['exp_form'] = exp_form
			if request.user.role == "Employer":
				return render(request, 'resume-detail-employer.html', context)
			else:
				return render(request, 'resume-detail.html', context)

	if request.method == 'GET':
		edu_form = EducationForm()
		exp_form = ExperienceForm()
		context['edu_form'] = edu_form
		context['exp_form'] = exp_form
		if request.user.role == "Employer":
			return render(request, 'resume-detail-employer.html', context)
		else:
			return render(request, 'resume-detail.html', context)

	if request.user.role == "Employer":
		return render(request, 'resume-detail-employer.html', context)
	else:
		return render(request, 'resume-detail.html', context)

def delete_experience(request, pk):
    exp = Experience.objects.get(pk=pk)  

    if request.method == 'POST':        
        exp.delete()                   
        messages.success(request, 'Experience deleted successfully')
        slug = request.user.resume.slug                         
        return redirect('resume_detail', slug=slug)            

    return render(request, 'resume_detail.html', {'exp': exp})

def delete_education(request, pk):
    edu = Education.objects.get(pk=pk)

    if request.method == 'POST':
        edu.delete()
        messages.success(request, 'Education deleted successfully')
        slug = request.user.resume.slug
        return redirect('resume_detail', slug=slug)

    return render(request, 'resume_detail.html', {'edu': edu})

@login_required
@user_passes_test(is_email_verified, 'verify_email', None)
def home_profiles(request):
	# search
	job_search_form = SearchJobsForm()

	context = {}
	context['job_search_form'] = job_search_form

	search_request = search(request)
	if search_request is not None:
		return search_request
	# end search

	#	can change to filter for search
	users_list = Account.objects.all()
	context['users'] = users_list
	return render(request, 'home_profiles.html', context)

@csrf_protect
def public_profile(request, slug):
    # search
    job_search_form = SearchJobsForm()
    model = ProjectImplicit.objects.all()
    context = {}
    context['job_search_form'] = job_search_form
    context['model'] = model
    search_request = search(request)
    if search_request is not None:
        return search_request
    # end search

    obj = Account.objects.get(slug=slug)

    try:
        if obj.resume:
            educations = Education.objects.filter(resume=obj.resume)
            experiences = Experience.objects.filter(resume=obj.resume)

            # essentially only true if theyre an employer and have this set up
            if obj.resume.company is not None:
                jobs = Job.objects.filter(company=obj.resume.company)
                context['postings'] = jobs

            context['educations'] = educations
            context['experiences'] = experiences    
    except Account.resume.RelatedObjectDoesNotExist:
        pass


    context['object'] = obj

    return render(request, 'public_profile.html', context)

def download(request, id, attrib_name):
    obj = Resume.objects.get(pk=id)
    if attrib_name == 'cover_letter':
        filename = obj.cover_letter.path
    elif attrib_name == 'cv':
        filename = obj.cv.path
    response = FileResponse(open(filename, 'rb'))
    return response 

def generateToken():
        API_KEY = 'yzOzjta3QuWlUY_hnXTP0w'
        API_SEC = 'vv4fId3KePvtmiRQipYicxGUIwbede4vudT7'

        token = jwt.encode(
            # Create a payload of the token containing API Key & expiration time
            {'iss': API_KEY, 'exp': time() + 5000},
            # Secret used to generate token signature
            API_SEC,
            # Specify the hashing alg
            algorithm='HS256'
            # Convert token to utf-8
            )
        return token
            # send a request with headers including a token

def sendEmail(emailAddr, emailDetails, subject):
    from_email = settings.EMAIL_HOST_USER
    to_email = [emailAddr]
    text_content = """
    {}
    {}
    {}
    {}          
        Best,
            The LinkedIncognito Team
                                                                                                    
                                                                                                            """.format(emailDetails['title'], emailDetails['subtitle'], emailDetails['message'], emailDetails['link'])
                                                                                                                                                                                 
    html_c = get_template('email.html')
    d = {'email': emailDetails}
    html_content = html_c.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def sendInvitation(invitee, employer, response):
    content = {}
    content['title'] = 'Hey There!'
    content['subtitle'] = 'You have been invited to an interview with ' + employer + '.'
    content['message'] = 'Here is the link to join your meeting ' + \
            response['join_url'] + ' at ' + response['start_time'] + '. If this time does not work for you, click the button below to notify your employer.'
    content['link'] = 'http://159.203.182.153:8000/sendRejection'

    subject = 'Interview Scheduled'
    sendEmail(invitee, content, "Interview Invitation")

def sendConfirmation(receiver, response):
    content = {}
    content['title'] = 'Hey There!'
    content['subtitle'] = 'You have successfully scheduled your interview.'
    content['message'] = 'Here is the link to start your meeting ' + \
            response['start_url'] + ' at ' + response['start_time']
    content['link'] = 'http://159.203.182.153:8000/'

    sendEmail(receiver, content, "Interview Scheduled")

@csrf_protect
def sendRejection(request):
        if request.method == "POST":
            receiver = Accounts.objects.get(username=request.POST["employer"])
            content = {}
            content['title'] = 'Hey There!'
            content['subtitle'] = request.user.username + ' has rejected your interview invitation.'
            content['message'] = 'Here is the link to schedule a new meeting:'
            content['link'] = 'http://159.203.182.153:8000/meetingCreation'

            sendEmail(receiver.email, content, "Interview Rejected")


@csrf_protect
def createMeeting(request):
    if request.method == "POST":

        meetingdetails = {"topic": request.POST["topic"],
                          "type": 2,

                          "start_time": request.POST["time"],
                          "duration": request.POST["duration"],
                          "timezone": "Eastern Time",
                          "agenda": "LinkedIncognito Interview", 
                          "settings": {"host_video": "true",
                                       "participant_video": "true",
                                       "join_before_host": "False",
                                       "mute_upon_entry": "False",
                                       "watermark": "true",
                                       "audio": "voip",
                                       "auto_recording": "cloud",
                                       "meeting_authentication": "False"
                                      }
                         }
        headers = {'authorization': 'Bearer %s' % generateToken(),
                'content-type': 'application/json'}
        
        r = requests.post(
                        f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))
  
       
        invitee = Account.objects.get(username=request.POST["invitee"])
        sendInvitation(invitee.email, request.user.first_name, r.json())
        sendConfirmation(request.user.email,r.json())

        return render(request, "meetingCreation.html", r.json())
    else:
        return render(request, "meetingCreation.html")

def email_verify_code(request):
    if request.method == 'GET':
        form = VerifyEmailForm()
        context = {'form' : form}
        return render(request, 'verify_email.html', context)

    if request.method == 'POST':
        form = VerifyEmailForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            try:
                usr = Account.objects.get(uniqueId=code)
                messages.success(request, 'Email verified, please log in')
                usr.email_confirmed = True
                usr.save()
                return redirect('login')
            except:
                messages.error(request, 'Sorry, that code is incorrect.')
                context = {'form': form}
                return render(request, 'verify_email.html', context)
        else:
            messages.error(request, 'Error processing your request')
            context = {'form': form}
            return render(request, 'verify_email.html', context)

    return render(request, 'verify_email.html', {})
