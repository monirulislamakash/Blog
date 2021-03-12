from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
class AllPost(models.Model):
    title=models.CharField(max_length=500,default="")
    post=models.TextField(default="")
    date=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title
class ProfilUpdate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    image=models.ImageField(upload_to="profile/",default="image/pro_avter.png")
    bio=models.TextField(default="Write Your 'Boi'")
    def __str__(self):
        return str(self.user)
    
    