from django.urls import re_path
from UserApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^applicant$', views.applicantApi),
    re_path(r'applicant/([0-9]+)$', views.applicantApi),

    re_path(r'^employer$', views.employerApi),
    re_path(r'employer/([0-9]+)$', views.employerApi),

    re_path(r'^job_posting$', views.jobPostingApi),
    re_path(r'job_posting/([0-9]+)$', views.jobPostingApi),

    re_path(r'^applicant/save_file$', views.SaveFile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)