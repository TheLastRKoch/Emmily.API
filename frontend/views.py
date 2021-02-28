from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')
