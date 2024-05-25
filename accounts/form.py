from django.forms import ModelForm
from . models import *
from django import forms
from django.utils import timezone

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['full_name', 'email', 'contact', 'account_type','post_code', 'company_name', 'about_company',]
        widgets = {
                'full_name': forms.TextInput(attrs={'class': 'col-md-6 form-control'}),
                'email': forms.EmailInput(attrs={'class': 'col-md-6 form-control'}),
                'contact': forms.TextInput(attrs={'class': 'col-md-6 form-control'}),
                'account_type': forms.Select(attrs={'class': 'col-md-6 form-control'}),
                'post_code': forms.TextInput(attrs={'class': 'col-md-6 form-control'}),
                'company_name': forms.TextInput(attrs={'class': 'col-md-6 form-control'}),
                'about_company': forms.Textarea(attrs={'class': 'col-md-12 form-control'}),
            }