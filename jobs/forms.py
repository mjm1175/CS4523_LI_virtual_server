from django import forms
from .models import *
from django.contrib.postgres.forms import SimpleArrayField


class CreateJobForm(forms.ModelForm):
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

    COMPUTER_SCIENCE = 'Computer Science'
    DATABASE_MANAGEMENT = 'Database Management'
    DATA_SCIENCE = 'Data Science'
    INFORMATION_SYSTEMS = 'Information Systems'
    NETWORK_SECURITY = 'Network Security'
    SOFTWARE_ENGINEERING = 'Software Engineering'
    WEB_DEVELOPMENT = 'Web Development'

    
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
    CAT_CHOICES = [
        (COMPUTER_SCIENCE, 'Computer Science'),
        (DATABASE_MANAGEMENT, 'Database Management'),
        (DATA_SCIENCE, 'Data Science'),
        (INFORMATION_SYSTEMS, 'Information Systems'),
        (NETWORK_SECURITY, 'Network Security'),
        (SOFTWARE_ENGINEERING, 'Software Engineering'),
        (WEB_DEVELOPMENT, 'Web Development'),
        (NOT_PROVIDED, 'N/A'),
    ]

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

    title = forms.CharField(
                max_length=150,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Job Title*'})
                )

    # new
    category = forms.ChoiceField(
                    required=False,
                    choices=CAT_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    )

    # new
    state = forms.ChoiceField(
                    required=False,
                    choices=STATE_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    )

    salary = forms.CharField(
                max_length=100,
                required=False,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Salary'})
                )
    
    # new
    city = forms.CharField(
                max_length=200,
                required=False,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'City'})
                )

    type = forms.ChoiceField(
                    required=True,
                    choices=TYPE_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    ) 

    experience = forms.ChoiceField(
                    required=False,
                    choices=EXP_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    ) 

    summary = forms.CharField(
                required=True,
                widget=forms.Textarea(attrs={'class':'form-control jobs', 'placeholder':'Summary*'})
                )

    description = forms.CharField(
                required=True,
                widget=forms.Textarea(attrs={'class':'form-control jobs', 'placeholder':'Description*'})
                )
    
    # new
    skills = SimpleArrayField(forms.CharField(max_length=100, required=False))

    
    class Meta:
        model=Job
        fields = [
            'title', 'salary', 'type', 'experience', 'summary', 'description',
            'skills', 'city', 'state', 'category'
        ]


class CreateCompanyForm(forms.ModelForm):
    name = forms.CharField(
                max_length=150,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control company', 'placeholder':'Company Name'})
                )    
    description = forms.CharField(
                required=False,
                widget=forms.Textarea(attrs={'class':'form-control jobs', 'placeholder':'Company Bio'})
                )    
    companyLogo = forms.ImageField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control'}),
                    )     

    class Meta:
        model=Company
        fields = [
            'name', 'description', 'companyLogo'
        ]           

class SearchJobsForm(forms.ModelForm):
    title = forms.CharField(
                        required=True,
                        widget=forms.TextInput(attrs={'class':'form-control rounded search-box', 'placeholder':'Search'})
    )

    class Meta:
        model = Job
        fields = ['title']

class ApplicationForm(forms.ModelForm):
    YES = 'Yes'
    NO = 'No'

    USE_RESUME_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    # won't show if the user doesn't have a resume
    use_profile_resume = forms.ChoiceField(
                    initial=NO,
                    choices=USE_RESUME_CHOICES,
                    widget=forms.RadioSelect(attrs={'class':'form-control', 'id':'prof-resume'}))
    use_profile_cover_letter = forms.ChoiceField(
                    initial=NO,
                    choices=USE_RESUME_CHOICES,
                    widget=forms.RadioSelect(attrs={'class':'form-control', 'id':'prof-cover'}))

    # this shows up if ^^ is No or if user doesnt have a resume
    resume = forms.FileField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control', 'id':'upload-resume'})
                    )
    cover_letter = forms.FileField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control', 'id':'upload-cover'})
                    )   

    location_type_ok = forms.BooleanField(required=True)
    
    class Meta:
        model = Application
        fields = [
            'use_profile_resume', 'use_profile_cover_letter', 'resume',
            'cover_letter', 'location_type_ok'
        ]    
