from django import forms
from django.contrib.auth.models import User
from .models import ProfilUpdate,AllPost
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "last_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "email":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
        }
        
class ProForm(forms.ModelForm):
    class Meta:
        model=ProfilUpdate
        fields=["image","bio"]
        widgets={
            "bio":forms.Textarea(attrs={"class":"form-control col-lg-3"})
        }
class PostEdit(forms.ModelForm):
    class Meta:
        model=AllPost
        fields=["title","post","date"]
        widgets={
                "title":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
                "post":forms.Textarea(attrs={"class":"form-control col-lg-3"})
            }