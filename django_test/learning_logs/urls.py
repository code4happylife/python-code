# encoding: utf-8
'''
@author: developer
@software: python
@file: urls.py
@time: 2020/8/30 15:47
@desc:
'''
"""定义learning_logs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
