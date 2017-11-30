from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<id>[0-9]+)/read/$', views.read, name='read'),
    url(r'^(?P<id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name='delete'),
]
