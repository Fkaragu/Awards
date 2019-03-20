from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^search/',views.search, name='search'),
    url(r'^theprojects/',views.projct),
    url(r'^upload/', views.upload_project, name='upload'),
    url(r'^profile/',views.profile),
    url(r'^editprofile/',views.editprofile, name='editprofile'),
    url(r'^rate/(\d+)',views.vote_project,name = 'rate'),
    url(r'^registrations/',views.register),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
