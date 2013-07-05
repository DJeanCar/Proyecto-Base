from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import IndexView
admin.autodiscover()

urlpatterns = patterns('',	
	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'logueo/login.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',
		name='logout'),
	url(r'^inicio/$', IndexView.as_view() , name='index'),

)