from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    # url(r'^frameworks/<framework_title>/$', views.frameworks, name='frameworks'),
    url(r'^frameworks/(?P<framework_id>\d+)/$', views.frameworks, name='frameworks'),
]
