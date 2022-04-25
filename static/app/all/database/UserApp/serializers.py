from rest_framework import serializers
from UserApp.models import Applicants, Employers, JobPosting

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicants
        fields=('Username', 'Password', 'Email', 'FirstName', 'LastName', 'Degree')

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employers
        fields=('Username', 'Password', 'Email', 'FirstName', 'LastName', 'CompanyName', 'ImplicitBiasFile')

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobPosting
        fields=('Title', 'JobType', 'Description')