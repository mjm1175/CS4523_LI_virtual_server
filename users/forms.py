from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Resume, Education, Experience

class RegisterForm(UserCreationForm):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)
    # maybe remove upload_to??
    image = models.ImageField(default='default.png', upload_to='profile_images')
    email_confirmed = models.BooleanField(default=False)
    # rm?
    date_birth = models.DateField(blank=True, null=True)
    # rm?
    sex = models.CharField(max_length=100, choices=SEX_CHOICES, default=OTHER)
    marital_status = models.CharField(max_length=100, choices=MARITAL_CHOICES, default=SINGLE)
    address_line1 = models.CharField(max_length=100, null=True, blank=True)
    address_line2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default=NY)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(null=True, blank=True)
    cover_letter = models.FileField(upload_to='resumes', null=True, blank=True)
    cv = models.FileField(upload_to='resumes', null=True, blank=True)
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
                    )

    password2 = forms.CharField(
                    required=True,
                    help_text='Enter Password Again',
                    widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'}),
                    )

    #check = forms.BooleanField(
    #                #required=True
    #                )

    #def save(self, *args, **kwargs):
    #    if not self.username:
    #        self.username = self.email
    #    super(Member, self).save(*args, **kwargs)

    class Meta:
        model = User

        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2'
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

    date_birth = forms.DateField(
                    required=True,
                    widget=DateInput(attrs={'class':'form-control', 'placeholder':'Enter a date: '})
                    )

    sex = forms.ChoiceField(
                    choices = SEX_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
                    )

    marital_status = forms.ChoiceField(
                    choices=MARITAL_CHOICES,
                    widget=forms.Select(attrs={'class':'nice-select rounded'})
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
    
    state = forms.CharField(
                    choices = STATE_CHOICES,
                    widget=forms.Select(attrs={'class': 'nice-select round'})
                    )

    phone_number = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Phone Number'})
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
            'image', 'date_birth', 'sex', 'marital_status', 'address_line1', 'address_line2',
            'city', 'state', 'phone_number', 'cover_letter', 'cv',
        ]
