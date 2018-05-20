from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', views.new_thread, name='new_thread'),
]