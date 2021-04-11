from django import forms
from .models import Portfolio

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICE=[
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chatisgarh','Chatisgarh')
]

class PortFolioForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Select Prefer Locations',
    choices=JOB_CITY_CHOICE,
    widget=forms.CheckboxSelectMultiple())
    class Meta:
        model=Portfolio
        fields=['name','dob','gender','locality','city','pin','state',
        'mobile','email','job_city','profile_image','my_file']

        labels={'name':'Full Name','dob':'Date Of Birth','pin':'PinCode',
        'mobile':'Mobile Number','email':'Email Id','profile_image':'Your Image','my_file':'Your Docs'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','label_sufix':' '}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
