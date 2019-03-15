from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^search/', views.search, name='search'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile')
]