"""amnh_turtle URL Configuration

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
from django.conf.urls import url

from . import views

app_name = 'turtle_observer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/(?P<expedition_id>[0-9]+)/(?P<location_id>[0-9]+)/$', views.new_turtle, name='new_turtle'),
    url(r'^observe/(?P<expedition_id>[0-9]+)/(?P<location_id>[0-9]+)/(?P<turtle_id>[0-9]+)/$', views.new_observation, name='new_observation'),
]