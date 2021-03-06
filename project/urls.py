"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import myApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myApp.views.index, name='index'),
    path('about/', myApp.views.about, name='about'),
    path('signin/', myApp.views.signin, name='signin'),
    path('signup/', myApp.views.signup, name='signup'),
    path('logout/', myApp.views.logout, name='logout'),
    path('chat/', myApp.views.chat, name='chat'),

    path('chatTest/', myApp.views.chatTest, name='chatTest'),


    path('dashboard/', myApp.views.dashboard, name='dashboard'),
    path('groupCalendar/', myApp.views.groupCalendar, name='groupCalendar'),
    path('individualCalendar/', myApp.views.individualCalendar, name='individualCalendar'),
    path('monitoringByPatient/', myApp.views.monitoringByPatient, name='monitoringByPatient'),
    path('monitoringByTime/', myApp.views.monitoringByTime, name='monitoringByTime'),

]
