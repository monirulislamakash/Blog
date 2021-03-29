from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="home" ),
    path('login',views.login,name="login" ),
    path('singup',views.singup,name="singup" ),
    path('logout',views.logout,name="logout" ),
    path('profile',views.profile,name="profile" ),
    path('post',views.post,name="post" ),
    path('updateprofile',views.updateprofile,name="updateprofile" ),
    path('delete/<int:id>/',views.delete,name="delete" ),
    path('update/<int:id>/',views.edite,name="edite" ),
    path('blog_support',views.support,name="support" ),


]
