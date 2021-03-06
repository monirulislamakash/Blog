from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import AllPost
from .models import ProfilUpdate
from .forms import UserForm,ProForm,PostEdit
from datetime import datetime
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        aiipost=AllPost.objects.order_by('-id')
        sendv={
            "post":aiipost
        }
        return render(request,"index.html",sendv)
    return redirect(login)
def singup(request):
    f_name=request.POST.get("f_name")
    l_name=request.POST.get("l_name")
    email=request.POST.get("email")
    passw=request.POST.get("password")
    cpassw=request.POST.get("confirmpassword")
    bio=request.POST.get("bio")
    propic=request.POST.get("propic")
    if request.method=="POST":
        if passw==passw:
            try:
                user=User.objects.get(username=email)
                return render(request,"singup.html",{'error':"User already exists"})  
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=cpassw,first_name=f_name,last_name=l_name)
                rfm=ProfilUpdate(image=propic,bio=bio)
                rfm.save()
                return render(request,"singup.html",{'success':"user created successfully"})    
        else:
            return render(request,"singup.html") 
    return render(request,"singup.html") 
def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"login.html",{'error':"Invalide User Password"})
    return render(request,"login.html") 
def logout(request):
    auth.logout(request)
    return redirect(index)
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    return redirect(login)
def post(request):
    if request.method=="POST":
        ptitel=request.POST.get("ptitel")
        posts=request.POST.get("post")
        fm=AllPost(title=ptitel,post=posts)
        fm.save()
    return render(request,"post.html")
def updateprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ufrom=UserForm(request.POST,instance=request.user)
            pfrom=ProForm(request.POST,request.FILES,instance=request.user.profilupdate)
            if ufrom.is_valid() and pfrom.is_valid():
                ufrom.save()
                pfrom.save()
                return render(request,"profile.html",{"error":"Profile Update successfully"})
        else:
            ufrom=UserForm(instance= request.user)
            pfrom=ProForm(instance= request.user.profilupdate)
        return render(request,"updateprofile.html",{"userfrom":ufrom,"profrom":pfrom})
    else:
        return redirect(login)
def delete(request,id):
    if request.method=="POST":
        pk=AllPost.objects.get(pk=id)
        pk.delete()
        return redirect(index)
def edite(request,id):
    if request.method=="POST":
        pk=AllPost.objects.get(pk=id)
        p_u_from=PostEdit(request.POST,instance=pk)
        if p_u_from.is_valid():
            p_u_from.save()
            return render(request,"postedit.html",{"editfrom":p_u_from})
    else:
        pk=AllPost.objects.get(pk=id)
        p_u_from=PostEdit(instance=pk)
        return render(request,"postedit.html",{"editfrom":p_u_from})
def support(request):
    if request.method=="POST":
        problem=request.POST.get("problem")
        feedback=request.POST.get("feedback")
        send_mail(
            problem,
            feedback,
            'monirulislamakash18@gmail.com',
            ['aaj7731@gmail.com'],
            fail_silently=False,
        )
        return render(request,"support.html",{'successfully':'we will get back to you soon'})
    return render(request,"support.html")
