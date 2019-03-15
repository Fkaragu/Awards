from django.shortcuts import render, redirect
from django.http import HttpResponse

def welcome (request):
    return render(request, 'master/index.html')

def search(request):
    message = 'Enter term to search'
    return render(request, 'search.html', {'message':message})

def profile(request):
    return render(request, 'profile/profile.html')

def proj(request):
    return render(request, 'project_upload.html')
