from django.conf.urls import url, include
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^hello/$', ListUsers.as_view(), name='hello'),
]
