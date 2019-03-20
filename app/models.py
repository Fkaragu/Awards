from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Project(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='articles/', blank=True)
    proj_title = models.CharField(max_length = 25)
    proj_link = models.CharField(max_length = 50)
    proj_description = models.CharField(max_length = 2500)
    design=models.PositiveIntegerField(choices=list(zip(range(1,11), range(1,11))), default=1)
    usability = models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    content = models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    remarks = models.CharField(max_length=50,null=True)
    post_date = models.DateTimeField(auto_now=True)
    
    def __str_(self):
        return self.proj_title

    def save_project(self):
        self.save()

    def update_project(self):
        self.update()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, name):
        pro = Project.objects.filter(proj_title__icontains = name)
        return pro

class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='articles/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    projects = models.ForeignKey(Project)
    contact = models.TextField(max_length=500, blank=True)

    def __str_(self):
        return self.contact

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()
