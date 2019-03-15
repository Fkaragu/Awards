from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm

def welcome (request):
    return render(request, 'master/index.html')

def search(request):
    message = 'Enter term to search'
    return render(request, 'search.html', {'message':message})

def profile(request):
    return render(request, 'profile/profile.html')

def proj(request):
    return render(request, 'project_upload.html')

def register(request):
    if request.user.is_authenticated():
        return redirect('home')
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
