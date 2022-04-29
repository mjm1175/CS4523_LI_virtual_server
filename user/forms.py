from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from .models import Resume, Education, Experience, Account

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


