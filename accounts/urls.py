
from django.urls import path
from . views import *


urlpatterns = [
    path('user_registration',UserRegistration, name="user_registration"),
 
] 

