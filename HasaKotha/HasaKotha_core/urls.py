"""HasaKotha_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.user_login_page, name='index'),
    path('login/', mainViews.user_login_page, name='login_page'),
    path('signup/', mainViews.user_signup_page, name='signup_page'),
    path('home/', mainViews.user_home_page, name='home_page'),
    #------------------------------------------------------------- page handling
    #goes to login page after signign up for an account
    path('signup_process/', mainViews.signup_process, name='signup_process'),
    path('login_process/', mainViews.login_process, name='login_process'),
]
