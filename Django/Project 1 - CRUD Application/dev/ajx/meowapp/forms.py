from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class Createuserform(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - login a user

class loginform(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class createrecord(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','province','country']


class updaterecord(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','province','country']


