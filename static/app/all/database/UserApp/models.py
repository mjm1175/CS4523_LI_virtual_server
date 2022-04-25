from django.db import models

# Create your models here.
class Applicants(models.Model):
    Username = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Degree = models.CharField(max_length=30)

class Employers(models.Model):
    Username = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    CompanyName = models.CharField(max_length=50)
    ImplicitBiasFile = models.CharField(max_length=500)

class JobPosting(models.Model):
    Title = models.AutoField(primary_key=True)
    JobType = models.CharField(max_length=20)
    Description = models.CharField(max_length=1000)

# class Interview(models.Model):
#     Employer = models.ForeignKey(Employers.Username)
#     Applicant = models.ForeignKey(Applicants.Username)
#     Date = models.Date()
#     Time = models.Time()


