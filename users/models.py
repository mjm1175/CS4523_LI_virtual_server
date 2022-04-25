from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Trying to have these be children of the generic user class thats a built-in, cant figure out how
class Applicants(User):
    degree = models.CharField(max_length=30)

class Employers(User):
    implicit_bias_file = models.CharField(max_length=500)

