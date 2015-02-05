from django.conf.urls import patterns, url

from index import views

urlpatterns = patterns('', 
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(ut_id>\d+)/$', views.detail, name='detail'),
    ('^time/$', views.current_datetime),
    ('^space/$', views.current_space),
    #url(r'^(?P<input_id>\d+)/results/$', views.results, name='result'),
)