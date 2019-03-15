from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'Login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'Login/logged_out.html'}, name='logout'),

    url(r'', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('registration.backends.simple.urls')),

]
