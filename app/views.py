from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def welcome(request):
    return render(request, 'master/index.html')

def upload_project(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return HttpResponse("Project has been uploaded successfully")
    else:
        form = UploadForm()
    return render(request,'upload_project.html',{'form':form})

def profile(request):
    proj = Project.objects.filter(user=request.user)
    prof = Profile.objects.filter(user=request.user)
    return render(request, 'profile/profile.html',{'prof':prof ,'proj':proj})

def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return HttpResponse("Profile has been updated successfully")
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

def projct(request):
    proj = Project.objects.all()
    return render(request, 'project_upload.html',{'proj':proj})

def register(request):
    if request.user.is_authenticated():
        return render(request,'master/index.html')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                return redirect(request, 'Login/success.html')
        else:
            form = SignupForm()
            return render(request, 'Login/signup.html',{'form':form})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        proj = Project.search_project(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'proj':proj})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
