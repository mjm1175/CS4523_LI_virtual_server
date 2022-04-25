from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Applicants, Employers, JobPosting
from UserApp.serializers import ApplicantSerializer, EmployerSerializer, JobPostingSerializer

from django.core.files.storage import default_storage
# Create your views here.

###################################### Applicant API #######################################
@csrf_exempt
def applicantApi(request, id=0):
    if request.method=='GET':
        applicants = Applicants.objects.all()
        applicants_serializer = ApplicantSerializer(applicants, many=True)
        return JsonResponse(applicants_serializer.data, safe=False)
    elif request.method=='POST':
        applicant_data = JSONParser().parse(request)
        applicants_serializer = ApplicantSerializer(data=applicant_data)
        if applicants_serializer.is_valid():
            applicants_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        applicant_data = JSONParser().parse(request)
        applicant = Applicants.objects.get(Username=applicant_data['Username'])
        applicants_serializer = ApplicantSerializer(applicant, data=applicant_data)
        if applicants_serializer.is_valid():
            applicants_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        applicant = Applicants.objects.get(Username=id)
        applicant.delete()
        return JsonResponse("Deleted Successfully", safe=False)

###################################### Employer API #######################################
@csrf_exempt
def employerApi(request, id=0):
    if request.method=='GET':
        employers = Employers.objects.all()
        employers_serializer = EmployerSerializer(employers, many=True)
        return JsonResponse(employers_serializer.data, safe=False)
    elif request.method=='POST':
        employer_data = JSONParser().parse(request)
        employers_serializer = EmployerSerializer(data=employer_data)
        if employers_serializer.is_valid():
            employers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        employer_data = JSONParser().parse(request)
        employer = Employers.objects.get(Username=employer_data['Username'])
        employers_serializer = EmployerSerializer(employer, data=employer_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        employer = Employer.objects.get(Username=id)
        employer.delete()
        return JsonResponse("Deleted Successfully", safe=False)

###################################### JobPosting API #######################################
@csrf_exempt
def jobPostingApi(request, id=0):
    if request.method=='GET':
        jobs = JobPosting.objects.all()
        jobs_serializer = JobPostingSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False)
    elif request.method=='POST':
        job_data = JSONParser().parse(request)
        jobs_serializer = JobPostingSerializer(data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        job_data = JSONParser().parse(request)
        job = JobPosting.objects.get(Title=job_data['Title'])
        jobs_serializer = JobPostingSerializer(job, data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        job = JobPosting.objects.get(Title=id)
        job.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
        file=request.FILES['file']
        file_name=default_storage.save(file.name, file)
        return JsonResponse(file_name, safe=False)


