from django.forms import ModelForm
from . models import *
from django import forms
from django.utils import timezone

class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields=["full_name", "email", "contact_number","message"]


class BrandForm(ModelForm):
    class Meta :
        model=Brand
        fields="__all__"

class PackageForm(ModelForm):
    class Meta :
        model=Q_Packages
        fields="__all__"


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['post', 'full_name', 'email', 'contact_number', 'about', 'indentification_card', 'cv', 'certificates']

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        # Get today's date
        today = timezone.now().date()
        # Filter jobs queryset to exclude expired jobs
        self.fields['post'].queryset = Jobs.objects.filter(application_deadline__gte=today)