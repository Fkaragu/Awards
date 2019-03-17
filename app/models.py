from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Project(models.Model):
    photo = models.ImageField(upload_to='articles/', blank=True)
    proj_name = models.CharField(max_length = 50)
    proj_link = models.CharField(max_length = 20)
    post_date = models.DateTimeField(auto_now=True)

    @classmethod
    def search_project(cls, name):
        pro = Project.objects.filter(proj_name__icontains = name)
        return pro
