from django.conf.urls import patterns, url

from ascii import views

urlpatterns = patterns('', 
     url(r'^$', views.index, name='index'),
     url(r'^(?P<input_id>\d+)/$', views.detail, name='detail'),
     url(r'^(?P<input_id>\d+)/results/$', views.results, name='result'),
)