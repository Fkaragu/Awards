from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Project(models.Model):
    photo = models.ImageField(upload_to='articles/', blank=True)
    photo_caption = models.CharField(max_length = 50)
    photo_link = models.CharField(max_length = 20)
    post_date = models.DateTimeField(auto_now=True)
