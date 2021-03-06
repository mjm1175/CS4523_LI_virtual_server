from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from uuid import uuid4
import random
from jobs.models import Company



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, role, first_name, last_name, password):
        if not email:
            raise ValueError("Users must have email address.")
        if not username:
            raise ValueError("Users must have username.")
        if not role:
            raise ValueError("Users must have role.")
        if not first_name:
            raise ValueError("Users must enter first name.")
        if not last_name:
            raise ValueError("Users must enter last name.")
        if not password:
            raise ValueError("Users must have password.")                                                

        user = self.model(
            email = self.normalize_email(email),
            password=password,
            username = username,  
            role = role,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user    

    def create_superuser(self, email, username, role, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username = username,  
            role = role,
            first_name = first_name,
            last_name = last_name       
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
    first_name = models.CharField(max_length=100, default="Owner")
    last_name = models.CharField(max_length=100, default = "Owner")
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=APPLICANT)
    email_confirmed = models.BooleanField(default=False)

    # allowing users to login using email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role', 'first_name', 'last_name']


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

    def get_absolute_url(self):
        return reverse('public_profile', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        # Creating a unique Identifier for the user (useful for other things in the future) && a SlugField for the url
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
        
        self.slug = slugify('{} {} {}'.format(self.first_name, self.last_name, self.uniqueId))

        super(Account, self).save(*args, **kwargs)


class Resume(models.Model):

    AK	= 'Alaska'
    AL	= 'Alabama'
    AR	= 'Arkansas'
    AZ	= 'Arizona'
    CA	= 'California'
    CO	= 'Colorado'
    CT	= 'Connecticut'
    DC	= 'District of Columbia'
    DE	= 'Delaware'
    FL	= 'Florida'
    GA	= 'Georgia'
    HI	= 'Hawaii'
    IA	= 'Iowa'
    ID	= 'Idaho'
    IL	= 'Illinois'
    IN	= 'Indiana'
    KS	= 'Kansas'
    KY	= 'Kentucky'
    LA	= 'Louisiana'
    MA	= 'Massachusetts'
    MD	= 'Maryland'
    ME	= 'Maine'
    MI	= 'Michigan'
    MN	= 'Minnesota'
    MO	= 'Missouri'
    MS	= 'Mississippi'
    MT	= 'Montana'
    NC	= 'North Carolina'
    ND	= 'North Dakota'
    NE	= 'Nebraska'
    NH	= 'New Hampshire'
    NJ	= 'New Jersey'
    NM	= 'New Mexico'
    NV	= 'Nevada'
    NY	= 'New York'
    OH	= 'Ohio'
    OK	= 'Oklahoma'
    OR	= 'Oregon'
    PA	= 'Pennsylvania'
    PR	= 'Puerto Rico'
    RI	= 'Rhode Island'
    SC	= 'South Carolina'
    SD	= 'South Dakota'
    TN	= 'Tennessee'
    TX	= 'Texas'
    UT	= 'Utah'
    VA	= 'Virginia'
    VT	= 'Vermont'
    WA	= 'Washington'
    WI	= 'Wisconsin'
    WV	= 'West Virginia'
    WY = 'Wyoming'

    STATE_CHOICES = [
        (AK,'Alaska'),
        (AL,'Alabama'),
        (AR,'Arkansas'),
        (AZ,'Arizona'),
        (CA,'California'),
        (CO,'Colorado'),
        (CT,'Connecticut'),
        (DC,'District of Columbia'),
        (DE,'Delaware'),
        (FL,'Florida'),
        (GA,'Georgia'),
        (HI,'Hawaii'),
        (IA,'Iowa'),
        (ID,'Idaho'),
        (IL,'Illinois'),
        (IN,'Indiana'),
        (KS,'Kansas'),
        (KY,'Kentucky'),
        (LA,'Louisiana'),
        (MA,'Massachusetts'),
        (MD,'Maryland'),
        (ME,'Maine'),
        (MI,'Michigan'),
        (MN,'Minnesota'),
        (MO,'Missouri'),
        (MS,'Mississippi'),
        (MT,'Montana'),
        (NC,'North Carolina'),
        (ND,'North Dakota'),
        (NE,'Nebraska'),
        (NH,'New Hampshire'),
        (NJ,'New Jersey'),
        (NM,'New Mexico'),
        (NV,'Nevada'),
        (NY,'New York'),
        (OH,'Ohio'),
        (OK,'Oklahoma'),
        (OR,'Oregon'),
        (PA,'Pennsylvania'),
        (PR,'Puerto Rico'),
        (RI,'Rhode Island'),
        (SC,'South Carolina'),
        (SD,'South Dakota'),
        (TN,'Tennessee'),
        (TX,'Texas'),
        (UT,'Utah'),
        (VA,'Virginia'),
        (VT,'Vermont'),
        (WA,'Washington'),
        (WI,'Wisconsin'),
        (WV,'West Virginia'),
        (WY,'Wyoming'),
    ]

    IMAGES = [
        'profile-pic1.jpg', 'profile-pic2.jpg', 'profile-pic3.jpg', 'profile-pic4.jpg', 'profile-pic5.jpg', 
        'profile-pic6.jpg', 'profile-pic7.jpg', 'profile-pic8.jpg', 'profile-pic9.jpg', 'profile-pic10.jpg', 
    ]

    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='default-job.png', upload_to='profile_images')
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default=NY) # choice
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    cover_letter = models.FileField(upload_to='resumes', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    cv = models.FileField(upload_to='resumes', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    # Applicants won't be able to add a company
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId)

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        # Creating a unique Identifier for the resume (useful for other things in the future) && a SlugField for the url
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
        
        self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.uniqueId))

        # assign a default profile image
        if self.image == 'default-job.png':
            self.image = random.choice(self.IMAGES)

        super(Resume, self).save(*args, **kwargs)

    
class Education(models.Model):
    # theres more
    LEVEL5A = 'Some High School Education'
    LEVEL5B = 'High School Certificate (G.E.D.)'
    LEVEL5C = 'High School Diploma'
    LEVEL6A = 'Some College Education'
    LEVEL6B = "Associate's Degree (AS/AA)"
    LEVEL6C = "Bachelor's Degree (BS/BA)"
    LEVEL7A = 'Some Postgraduate School'
    LEVEL7B = 'Professional School Graduate'
    LEVEL7C = "Master's Degree (MS/MA)"
    LEVEL8 = "Doctorate's Degree (PHD)"

    LEVEL_CHOICES = [
        (LEVEL5A, 'Some High School Education'),
        (LEVEL5B, 'High School Certificate (G.E.D.)'),
        (LEVEL5C, 'High School Diploma'),
        (LEVEL6A, 'Some College Education'),
        (LEVEL6B, "Associate's Degree (AS/AA)"),
        (LEVEL6C, "Bachelor's Degree (BS/BA)"),
        (LEVEL7A, 'Some Postgraduate School'),
        (LEVEL7B, 'Professional School Graduate'),
        (LEVEL7C, "Master's Degree (MS/MA)"),
        (LEVEL8, "Doctorate Degree (PHD)"),
    ]


    institution = models.CharField(null=True, blank=True, max_length=200)
    level = models.CharField(choices=LEVEL_CHOICES, default=LEVEL5A, max_length=200)
    start_date = models.DateField(null=True, blank=True)
    graduated = models.DateField(blank=True, null=True)
    major_subject = models.CharField(null=True, blank=True, max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    def __str__(self):
        return '{} for {} {}'.format(self.institution, self.resume.user.first_name, self.resume.user.last_name)
       
class Experience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(null=True, blank=True, max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    skills = ArrayField(models.CharField(max_length=100, null=True, blank=True), default=list)
    date_created = models.DateTimeField(default=timezone.now)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return '{} at {}'.format(self.position, self.company)

class ProjectImplicit(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')
    project_implicit = models.FileField(upload_to='project-implicit', null=True, blank=True)

class MeetingZoom(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')
    interviewer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    meeting_date = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField()
    link = models.CharField(null=True, blank=True, max_length=300)
