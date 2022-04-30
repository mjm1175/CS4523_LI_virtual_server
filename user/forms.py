from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.postgres.forms import SimpleArrayField

from .models import *


class RegisterForm(forms.ModelForm):

    EMPLOYER = 'Employer'
    APPLICANT = 'Applicant'

    ROLE_CHOICES = [
        (EMPLOYER, 'Employer'),
        (APPLICANT, 'Applicant')
    ]

    email = forms.EmailField(
                    max_length=100,
                    required=True,
                    help_text='Enter Email Address',
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                    )
 
    first_name = forms.CharField(
                    max_length=100,
                    required=True,
                    help_text='Enter First Name',
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                    )

    last_name = forms.CharField(
                    max_length=100,
                    required=True,
                    help_text='Enter Last Name',
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
                    )

    username = forms.CharField(
                    max_length=200,
                    required = False,
                    help_text='Enter Username',
                    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
                    )

    password1 = forms.CharField(
                    help_text='Enter Password',
                    required=True,
                    )

    password2 = forms.CharField(
                    required=True,
                    help_text='Enter Password Again',
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'}),
                    )

    role = forms.ChoiceField(
                    choices=ROLE_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    )

    #check = forms.BooleanField(
    #                #required=True
    #                )

    #def save(self, *args, **kwargs):
    #    if not self.username:
    #        self.username = self.email
    #    super(Member, self).save(*args, **kwargs)

    class Meta:
        model = Account

        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role'
        ]


class DateInput(forms.DateInput):
    input_type = 'date'

class ResumeForm(forms.ModelForm):
    # seems like we wont be using these LMFAO
    MALE = 'Male'
    FEMALE = 'Female'
    NONBINARY = 'Nonbinary'
    OTHER = 'Other'
    MARRIED = 'Married'
    SINGLE = 'Single'
    WIDOWED = 'Widowed'
    DIVORCED = 'Divorced'

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

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Nonbinary'),
        (OTHER, 'Other'),
    ]

    MARITAL_CHOICES = [
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (WIDOWED, 'Widowed'),
        (DIVORCED, 'Divorced'),
    ]

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

    image = forms.ImageField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control'}),
                    )

    address_line1 = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Enter Address Line 1'}),
                    )
    
    address_line2 = forms.CharField(
                    required=False,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Enter Address Line 2'})
                    )
    
    city = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter City'})
                    )
    
    state = forms.ChoiceField(
                    choices = STATE_CHOICES,
                    widget=forms.Select(attrs={'class': 'nice-select round'})
                    )
    
    cover_letter = forms.FileField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control'})
                    )

    cv = forms.FileField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control'})
                    )

    class Meta:
        model = Resume
        fields = [
            'image', 'address_line1', 'address_line2',
            'city', 'state', 'cover_letter', 'cv',
        ]




class EducationForm(forms.ModelForm):
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

    institution = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Name of Institution'})
                    )
    qualification = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Name of Qualification'})
                    )
    level = forms.ChoiceField(
                    choices=LEVEL_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    )   
    start_date = forms.DateField(
                    required=True,
                    widget=DateInput(attrs={'class':'form-control', 'placeholder':'Enter a date: '})
                    )
    graduated = forms.DateField(
                    required=True,
                    widget=DateInput(attrs={'class':'form-control', 'placeholder':'Enter a date: '})
                    )
    major_subject = forms.CharField(
                    required=False,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Major Subjects'})
                    )

    class Meta:
        model=Education
        fields = [
            'institution', 'qualification', 'level', 'start_date', 'graduated', 'major_subject'
        ]





class ExperienceForm(forms.ModelForm):
    company = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Company Worked For'})
                    )
    
    position = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Position/Role'})
                    )

    start_date = forms.DateField(
                    required=True,
                    widget=DateInput(attrs={'class':'form-control', 'placeholder':'Enter a date: '})
                    )                    

    end_date = forms.DateField(
                    required=True,
                    widget=DateInput(attrs={'class':'form-control', 'placeholder':'Enter a date: '})
                    )

    experience = forms.CharField(
                    required=False,
                    widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter experience'})
                    )

    #skills = forms.CharField(
    #                required=False,
    #                widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Enter skills'})
    #                #widget=forms.TextInput(attrs={'class':'form-control resume', 'placeholder':'Enter skills separated by commas'})
    #                )

    skills = SimpleArrayField(forms.CharField(max_length=100, required=False))

    class Meta:
        model=Experience
        fields = [
            'company', 'position', 'start_date', 'end_date', 'experience', 'skills'
        ]
