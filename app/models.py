from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Project(models.Model):
    photo = models.ImageField(upload_to='articles/', blank=True)
    proj_title = models.CharField(max_length = 25)
    proj_link = models.CharField(max_length = 50)
    proj_description = models.CharField(max_length = 2500)
    post_date = models.DateTimeField(auto_now=True)

    @classmethod
    def search_project(cls, name):
        pro = Project.objects.filter(proj_title__icontains = name)
        return pro
