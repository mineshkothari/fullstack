"""fullstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin
from django.views.static import serve
from settings import MEDIA_ROOT

urlpatterns = [
    # ADMIN
    url(r'^admin/', admin.site.urls),

    # HOME
    url(r'^', include('home.urls')),

    # ABOUT
    # url(r'^about/', include('django.contrib.flatpages.urls')),
    url(r'^about/', include('about.urls')),

    # ACCOUNTS
    url(r'^account/', include('accounts.urls')),

    # BLOG
    url(r'^blog/', include('blog.urls')),

    # FORUM
    url(r'^forum/', include('forum.urls')),

    # COURSES
    url(r'^courses/', include('courses.urls')),

    # CART
    url(r'^cart/', include('cart.urls')),

    # CHECKOUT
    url(r'^checkout/', include('checkout.urls')),

    # MEDIA
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # # DJANGO-SUMMERNOTE
    # url(r'^summernote/', include('django_summernote.urls')),
]

# CUSTOM 404 HANDLER
handler404 = 'home.views.my_custom_page_not_found_view'

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
