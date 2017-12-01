from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^create/$', views.create, name='create'),
    url(r'^read/(?P<id>[0-9]+)/$', views.read, name='read'),
    url(r'^update/(?P<id>[0-9]+)/$', views.update, name='update'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
]
