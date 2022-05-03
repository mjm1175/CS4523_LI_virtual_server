from email.policy import default
from django.db import models
from django.utils import timezone
from user.models import Account
from uuid import uuid4
from django.template.defaultfilters import slugify

# Example model
class Job(models.Model):
    # these values are what will actually be stored in the database
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    REMOTE = 'RT'
    TIER1 = 't1'
    TIER2 = 't2'
    TIER3 = 't3'
    TIER4 = 't4'
    TIER5 = 't5'
    
    # Pairing backend values with front end displays
    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (REMOTE, 'Remote'),
    ]
    EXP_CHOICES = [
        (TIER1, 'Less than 2yrs'),
        (TIER2, '2yrs - 5yrs'),
        (TIER3, '5yrs - 10yrs'),
        (TIER4, '10yrs - 15yrs'),
        (TIER5, 'More than 15yrs'),
    ]

    title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=FULL_TIME)
    experience = models.CharField(max_length=10, choices=EXP_CHOICES, default=TIER1)
    summary = models.TextField()
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(default='default-job.png', upload_to='upload_images')
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)    # might should change User to Company?

    #owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    # might should change User to Company?
    # models.CASCADE means that if user gets deleted, the job will be deleted with them

    def __str__(self):
        return '{} looking for {}'.format(self.company, self.title)

    def get_absolute_url(self):
        return reverse('job_post', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        # Creating a unique Identifier for the user (useful for other things in the future) && a SlugField for the url
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
        
        self.slug = slugify('{} {} {}'.format(self.title, self.company, self.uniqueId))

        super(Job, self).save(*args, **kwargs)
