from django.contrib import admin
from .models import Applicants, Employers

# Register your models here.
admin.site.register(Applicants)
admin.site.register(Employers)
