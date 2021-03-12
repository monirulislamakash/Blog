from django import forms
from django.contrib.auth.models import User
from .models import ProfilUpdate
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
class ProForm(forms.ModelForm):
    class Meta:
        model=ProfilUpdate
        fields=["image"]