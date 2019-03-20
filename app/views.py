from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
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

def vote_project(request, project_id):
  project = Project.objects.get(id=project_id)
  rating = round(((project.design + project.usability + project.content)/3),2)
  if request.method == 'POST':
      form = VoteForm(request.POST)
      if form.is_valid:
          if project.design == 1:
              project.design = int(request.POST['design'])
          else:
              project.design = (project.design + int(request.POST['design']))/2
          if project.usability == 1:
              project.usability = int(request.POST['usability'])
          else:
              project.usability = (project.design + int(request.POST['usability']))/2
          if project.content == 1:
              project.content = int(request.POST['content'])
          else:
              project.content = (project.design + int(request.POST['content']))/2
          project.save()
  else:
      form = VoteForm()
  return render(request,'vote.html',{'form':form,'project':project,'rating':rating})

def project(request, project_id):
   try:
       project = Project.objects.get(id = project_id)
       rating = round(((project.design + project.usability + project.content) / 3), 2)
       if request.method == 'POST':
           form = VoteForm(request.POST)
           if form.is_valid:
               if project.design == 1:
                   project.design = int(request.POST['design'])
               else:
                   project.design = (project.design + int(request.POST['design'])) / 2
               if project.usability == 1:
                   project.usability = int(request.POST['usability'])
               else:
                   project.usability = (project.design + int(request.POST['usability'])) / 2
               if project.content == 1:
                   project.content = int(request.POST['content'])
               else:
                   project.content = (project.design + int(request.POST['content'])) / 2
               project.save()
       else:
           form = VoteForm()
   except DoesNotExist:
       raise Http404()
   return render(request,"project.html", {'form': form, 'project': project, 'rating': rating})

class ProjectList(APIView):
  def get(self, request, format=None):
      all_proj = Project.objects.all()
      serializers = ProjectSerializer(all_proj, many=True)
      return Response(serializers.data)

class ProfileList(APIView):
  def get(self, request, format=None):
      all_profile = Project.objects.all()
      serializers = ProfileSerializer(all_profile, many=True)
      return Response(serializers.data)
