from django import forms
from .models import Nexus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NexusForm(forms.ModelForm):
    class Meta:
        model=Nexus
        fields=['text','photo']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model:User
        fields=('username','password1','password2')
        
