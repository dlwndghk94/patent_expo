# encoding: utf-8
from django.conf.urls import include, url
from fileupload.views import (
        FileCreateView, FileDeleteView, FileListView, predict
    )

urlpatterns = [
    url(r'^home/$', FileCreateView.as_view(), name='upload-new'),
    url(r'^delete/(?P<pk>\d+)$', FileDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', FileListView.as_view(), name='upload-view'),
    url(r'^predict/$', predict, name='predict'),
]
