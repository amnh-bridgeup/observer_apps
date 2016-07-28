"""amnh_observer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

try:
    from django.conf.urls.defaults import *
except ImportError:
    from django.conf.urls import include, patterns, url

from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^', include('turtle_observer.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'turtle_observer/registration/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'turtle_observer/registration/logout.html'}),
    url(r'^password_reset/$', auth_views.password_reset),
    url(r'^admin/', include(admin.site.urls)),
]
