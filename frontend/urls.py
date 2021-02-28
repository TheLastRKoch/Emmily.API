from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import  frontend.views

urlpatterns = [
    
    path('', frontend.views.index)
]
