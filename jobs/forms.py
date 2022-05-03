from django import forms
from .models import *

class CreateJobForm(forms.ModelForm):
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

    title = forms.CharField(
                max_length=150,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Job Title'})
                )

    company = forms.CharField(
                max_length=100,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Company Name'})
                )

    location = forms.CharField(
                max_length=200,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Location'})
                )

    salary = forms.CharField(
                max_length=100,
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Salary'})
                )

    type = forms.ChoiceField(
                    choices=TYPE_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    ) 

    experience = forms.ChoiceField(
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
                required=True,
                widget=forms.TextInput(attrs={'class':'form-control jobs', 'placeholder':'Requirements'})
                )

    logo = forms.ImageField(
                    required=False,
                    widget=forms.FileInput(attrs={'class':'form-control'})
                    )
    
    class Meta:
        model=Job
        fields = [
            'title', 'company', 'location', 'salary', 'type', 'experience', 'summary', 'description',
            'requirements', 'logo'
        ]

