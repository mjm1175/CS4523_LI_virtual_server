from django import forms
from .models import *

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
    title = forms.CharField(
                max_length=150,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Job Title'})
                )

    location = forms.CharField(
                max_length=200,
                required=False,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Location'})
                )

    salary = forms.CharField(
                max_length=100,
                required=False,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Salary'})
                )

    type = forms.ChoiceField(
                    required=False,
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
                widget=forms.Textarea(attrs={'class':'form-control jobs', 'placeholder':'Summary'})
                )

    description = forms.CharField(
                required=True,
                widget=forms.Textarea(attrs={'class':'form-control jobs', 'placeholder':'Description'})
                )

    requirements = forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Requirements'})
                )
    
    closing_date = forms.DateField(
                    required=False,
		    widget=forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'class': 'datepicker', 'placeholder': 'Select a date', 
					    'type': 'date', 'placeholder':'Select a date'})
                    )
    
    class Meta:
        model=Job
        fields = [
            'title', 'company', 'location', 'salary', 'type', 'experience', 'summary', 'description',
            'requirements', 'closing_date'
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
    upload_resume = forms.FileField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control', 'id':'upload-resume'})
                    )
    upload_cover_letter = forms.FileField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control', 'id':'upload-cover'})
                    )   

    location_type_ok = forms.BooleanField(required=True)
    
    class Meta:
        model = Application
        fields = [
            'use_profile_resume', 'use_profile_cover_letter', 'upload_resume',
            'upload_cover_letter', 'location_type_ok'
        ]    
