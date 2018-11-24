from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    url(r'^modules/(?P<language_id>\d+)/$', views.modules, name='modules'),
    url(r'^unit/(?P<module_id>\d+)/$', views.module_item, name='module_item'),
    url(r'^new-module/$', views.new_module, name='new_module'),
]
