"""LIapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from jobs import views as jobs_views
from user import views as users_views
from user import forms as user_forms
from messenger import views as msg_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs_views.home, name='home_page'),
    path('job-post/<slug:slug>/', jobs_views.job_post, name='job_post'),
    path('create-job/', jobs_views.job_post_creation, name='job_post_creation'),
    path('jobs/company/<slug:slug>', jobs_views.company_detail, name='company_detail'),
    path('create-company/', jobs_views.company_creation, name='company_creation'),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('users/create/', users_views.create_resume, name='create_resume'),
    path('users/create/<int:res_id>', users_views.create_resume, name='create_resume'),
    path('users/view/<slug:slug>/', users_views.resume_detail, name='resume_detail'),
    path('users/delete/experience/<int:pk>/', users_views.delete_experience, name='delete_experience'),
    path('users/delete/education/<int:pk>/', users_views.delete_education, name='delete_education'),
    path('users/public-profile/<slug:slug>/', users_views.public_profile, name='public_profile'),
    path('all-users/', users_views.home_profiles, name='all_users'),
    path('all-companies/', jobs_views.home_companies, name='all_companies'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('download/<str:attrib_name>/<int:id>/', users_views.download, name='download'),
    # this one might be useless now?
    path('messenger/', msg_views.messenger, name='messenger'),
    path('inbox/', msg_views.ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread', msg_views.CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', msg_views.ThreadView.as_view(), name='thread'),

    path('inbox/<int:pk>/create-message', msg_views.CreateMessage.as_view(), name='create-message'),
    
    path('zoom/callback/', users_views.zoom_callback, name='zoom_callback'),
    path('meetingCreation/', users_views.schedule_interview, name='schedule_interview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
