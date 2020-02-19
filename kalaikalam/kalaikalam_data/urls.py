from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    # url('^details/$', views.display_detail, name='details')
]
