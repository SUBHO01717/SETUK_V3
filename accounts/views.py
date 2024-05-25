from django.shortcuts import render, redirect
from django.contrib import messages
from .form import *
from . models import *
# Create your views here.


def UserRegistration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been successfully submitted. One of our execute will contact shortly for verification purpose')
            return redirect('/')  # Replace 'success_url_name' with your actual success URL name
    else:
            form = RegistrationForm()

    return render(request, 'register.html', {'form': form})