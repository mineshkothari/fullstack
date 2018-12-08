from django.conf.urls import url
from .views import view_cart, add_to_cart


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<module_id>\d+)$', add_to_cart, name='add_to_cart'),
    # url(r'^delete/(?P<module_id>\d+)$', remove_from_cart, name='remove_from_cart'),
]
