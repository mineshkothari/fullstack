from django.conf.urls import url, include
from . import views
from . import urls_reset

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^password-reset/', include(urls_reset))
]
