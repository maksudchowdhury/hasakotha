from operator import truediv
import re
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from pip import main
from mainapp import models as mainModels
from django.contrib import messages





# -------------------------------------------------------------  Page rendering section starts
def user_signup_page(request):
    return render(request,'signup.html',None)
def user_login_page(request):
    return render(request,'login.html',None)
def user_home_page(request):
    return render (request,'home.html',None)
def share_message_page(request):
    return render (request,'passMessage.html',None)

# ------------------------------------------------------------- Page handling section starts




def signup_process(request):
    user_firstname= request.POST.get('firstName')
    user_lastname= request.POST.get('lastName')
    user_email= request.POST.get('email')
    user_nickName= request.POST.get('nickName')
    user_password= request.POST.get('password')
    user_confirmPassword= request.POST.get('confirmPassword')

    nickName_count = mainModels.user_info.objects.filter(nickname=user_nickName).count()
    email_count = mainModels.user_info.objects.filter(nickname=user_nickName).count() #we can use this for maintaining unique email system
    if nickName_count == 0:
        if user_password == user_confirmPassword:
            mainModels.user_info.objects.create(first_name=user_firstname, last_name=user_lastname, email=user_email, nickname=user_nickName, password= user_password)
            request.session['signup_success']=True
            request.session['signup_error']=False
            request.session['nickName_duplicate']=False
            return redirect('login_page')
        else:
            request.session['signup_error']=True
            return redirect('signup_page')
    else:
        request.session['nickName_duplicate']=True
        return redirect('signup_page')

def login_process(request):
    request.session['login_error']=False
    request.session['signup_success']=False
    user_nickName = request.POST.get('nickName')
    user_password = request.POST.get('password')
    count = mainModels.user_info.objects.filter(nickname=user_nickName,password=user_password).count()
    if count == 1:
        return redirect('home_page')
    else:
        request.session['login_error']=True
        messages.warning(request, 'Invalid Username or Password')
        messages.success(request, 'also we are able to show the warning successfully')
        return redirect('login_page')