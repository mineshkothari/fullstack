from django.conf.urls import url
from .views import checkout, checkout_login


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^login/$', checkout_login, name='checkout_login'),
]
