from django.forms import ModelForm
from . models import *
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields=["full_name", "email", "contact_number","message"]


class BrandForm(ModelForm):
    class Meta :
        model=Brand
        fields="__all__"