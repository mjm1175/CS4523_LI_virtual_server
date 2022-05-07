from email.policy import default
from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.template.defaultfilters import slugify


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    companyLogo = models.ImageField(default='default-job.png', upload_to='upload_images')
    slug= models.SlugField(max_length=500, unique=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
        
        self.slug = slugify('Company {} {}'.format(self.name, self.uniqueId))
        super(Company, self).save(*args, **kwargs)



from user.models import Account

class Job(models.Model):
    # these values are what will actually be stored in the database
    FULL_TIME = 'Full Time'
    PART_TIME = 'Part Time'
    REMOTE = 'Remote'
    NOT_PROVIDED = 'N/A'
    TIER1 = 'Less than 2yrs'
    TIER2 = '2yrs - 5yrs'
    TIER3 = '5yrs - 10yrs'
    TIER4 = '10yrs - 15yrs'
    TIER5 = 'More than 15yrs'
    
    # Pairing backend values with front end displays
    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (REMOTE, 'Remote'),
        (NOT_PROVIDED, 'N/A')
    ]
    EXP_CHOICES = [
        (TIER1, 'Less than 2yrs'),
        (TIER2, '2yrs - 5yrs'),
        (TIER3, '5yrs - 10yrs'),
        (TIER4, '10yrs - 15yrs'),
        (TIER5, 'More than 15yrs'),
        (NOT_PROVIDED, 'N/A')
    ]

    title = models.CharField(max_length=150, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True) # choice
    salary = models.CharField(max_length=100, null=True, blank=True) # choice
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=NOT_PROVIDED) # choice
    experience = models.CharField(max_length=100, choices=EXP_CHOICES, default=NOT_PROVIDED)
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True) # array???
    #applications = models.TextField(null=True, blank=True)
    closing_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)    # might should change User to Company?
    # models.CASCADE means that if user gets deleted, the job will be deleted with them

    def __str__(self):
        return '{} looking for {}'.format(self.company, self.title)

    def get_absolute_url(self):
        return reverse('job_post', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        # Creating a unique Identifier for the user (useful for other things in the future) && a SlugField for the url
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
        
        # can i change location back to company?
        self.slug = slugify('{} {} {}'.format(self.title, self.location, self.uniqueId))

        super(Job, self).save(*args, **kwargs)


class Application(models.Model):
    applicant = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    # say something liek if resume else add a resume to your profile to submit more info
    #choice to include resume from profile or add new one (will not replace profile resume)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    cover_letter = models.FileField(upload_to='resumes', null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}'s application to {}".format(self.applicant.username, self.job.title)    

