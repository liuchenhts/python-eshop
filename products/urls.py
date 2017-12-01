from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^create/$', views.create, name='create'),
    # use pk as request parameter in favor of generic  views
    url(r'^read/(?P<pk>[0-9]+)/$', views.read, name='read'),
    # url(r'^read/(?P<pk>[0-9]+)/$', views.read.as_view(), name='read'), # generic view
    url(r'^update/(?P<pk>[0-9]+)/$', views.update, name='update'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name='delete'),
]
