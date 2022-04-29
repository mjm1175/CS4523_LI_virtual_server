from django.contrib import admin
from .models import Account, Resume, Education, Experience

# Register your models here.
admin.site.register(Account)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
