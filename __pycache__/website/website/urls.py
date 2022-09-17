"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from signup.views import signaction
from login.views import loginaction
from dashboard.views import dashboard
from dashboard import views
from telebot.views import telebot
from telebot.views import update
from telebot.views import bot_update
from telebot.views import form
from telebot.views import deleterow
from edit.views import editpage
from edit.views import update1
from django.urls import include

# from dashboard.views import board
from login import views
#from telebot import views
#rom telebot import views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('signup/',signaction),
     path('login/',loginaction),
     path('dashboard/',dashboard),
     path('telebot/',telebot),
     path('update/',update),
     path('bot_update/',bot_update),
     path('form/',form),
     path('deleterow/',deleterow),
     path('editpage/',editpage),
     path('update1/',update1),
    #path('', include('base.urls')),
    #path("index/", views.projects, name="index"),
    path('', views.loginaction),
    #path('',views.showform)
    #path('',views.dashboard)
    #path('',views.telebot)
    #path('',views.telebot)
    #path('',views.show)

]
