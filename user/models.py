from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
import random

# Create your models here.

# override user class
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email address.")
        if not username:
            raise ValueError("Users must have username.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user    

    def create_superuser(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            password=password,
            username = username,         
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user  


class Account(AbstractBaseUser):

    EMPLOYER = 'Employer'
    APPLICANT = 'Applicant'

    ROLE_CHOICES = [
        (EMPLOYER, 'Employer'),
        (APPLICANT, 'Applicant')
    ]

    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    # begin required
    username = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # end required
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    #uniqueId = models.CharField(max_length=100, null=True, blank=True)
    #role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=APPLICANT)

    # allowing users to login using email
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username', 'role', 'first_name', 'last_name']
    REQUIRED_FIELDS = ['username']


    objects = MyAccountManager()

    def __str__(self):
        #return '{} {} {}'.format(self.first_name, self.last_name, self.uniqueId)
        return self.email

    # begin required
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    # end required

    #def get_absolute_url(self):
    #    return reverse('public_profile', kwargs={'slug': self.slug})
    
    #def save(self, *args, **kwargs):
        # Creating a unique Identifier for the resume (useful for other things in the future) && a SlugField for the url
    #    if self.uniqueId is None:
    #        self.uniqueId = str(uuid4()).split('-')[0]
        
    #    self.slug = slugify('{} {} {}'.format(self.first_name, self.last_name, self.uniqueId))

    #    super(Resume, self).save(*args, **kwargs)
