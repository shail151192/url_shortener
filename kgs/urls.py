from django.conf.urls import include, url
from django.contrib import admin
from kgs.views import *

urlpatterns = [
    url(r'$', KgsListView.as_view())
]
