# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url

from . import views
import spirit.category.admin.urls
import spirit.comment.flag.admin.urls
import spirit.topic.admin.urls
import spirit.user.admin.urls


urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^config/$', views.config_basic, name='config-basic'),

    url(r'^category/', include(spirit.category.admin.urls, namespace='category')),
    url(r'^comment/flag/', include(spirit.comment.flag.admin.urls, namespace='flag')),
    url(r'^topic/', include(spirit.topic.admin.urls, namespace='topic')),
    url(r'^user/', include(spirit.user.admin.urls, namespace='user')),
]
