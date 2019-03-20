from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('user','photo','proj_title','proj_link','proj_description')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','profile_pic','bio','projects','contact')

class VoteForm(forms.ModelForm):
    class Meta:
       model = Project
       fields=('design','usability','content','remarks')
