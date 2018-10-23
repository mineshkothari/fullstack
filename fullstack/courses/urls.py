from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    url(r'^languages/(?P<framework_id>\d+)/$', views.languages, name='languages'),
]
