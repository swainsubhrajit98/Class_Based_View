"""Project30 URL Configuration

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
from App.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('FBV_String/',FBV_String,name='FBV_String'),
    path('CBV_String/',CBV_String.as_view(),name='CBV_String'),

    path('FBV_Page/',FBV_Page,name='FBV_Page'),
    path('CBV_Page/',CBV_Page.as_view(),name='CBV_Page'),

    path('FBV_Form/',FBV_Form,name='FBV_Form'),
    path('CBV_Form/',CBV_Form.as_view(),name='CBV_Form'),

    path('CBV_Template/',CBV_Template.as_view(),name='CBV_Template'),
]
