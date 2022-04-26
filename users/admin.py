from django.contrib import admin
from .models import Applicants, Employers, Resume, Education, Experience

# Register your models here.
admin.site.register(Applicants)
admin.site.register(Employers)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
