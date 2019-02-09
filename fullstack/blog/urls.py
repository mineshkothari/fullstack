from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='blog'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^top/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^top/$', views.top_posts, name='top_posts'),
    url(r'^post/new/$', views.new_blog_post, name='new_blog_post'),
    url(r'^(?P<post_id>\d+)/edit$', views.edit_post, name='edit'),
]
