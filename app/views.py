from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from .models import Project

def welcome (request):
    return render(request, 'master/index.html')

def profile(request):
    return render(request, 'profile/profile.html')

def projct(request):
    proj = Project.objects.all()
    return render(request, 'project_upload.html',{'proj':proj})

def register(request):
    if request.user.is_authenticated():
        return redirect('welcome')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                return render(request, 'Login/success.html')
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
