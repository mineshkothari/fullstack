from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', views.threads, name='threads'),
]