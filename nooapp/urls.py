from django.conf.urls import url

from . import views

app_name = 'nooapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'call/$', views.call, name='call'),
    url(r'conf/$', views.conf, name='conf'),
]
