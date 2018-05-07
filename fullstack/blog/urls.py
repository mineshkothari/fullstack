from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^top/$', views.top_posts, name='top_posts'),
]
