from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    url(r'^languages/(?P<framework_id>\d+)/$', views.languages, name='languages'),
    url(r'^modules/(?P<language_id>\d+)/$', views.modules, name='modules'),
    url(r'^unit/(?P<module_id>\d+)/$', views.module_item, name='module_item'),
]
