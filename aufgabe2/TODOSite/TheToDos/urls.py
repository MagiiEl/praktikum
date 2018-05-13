# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('ubersicht.html/', views.ubersicht, name ='ubersicht'),
        path('impressum.html/', views.impressum, name ='impressum'),
        path('edittodo.html/', views.edittodo, name ='edittodo'),
        path('newtodo.html/', views.newtodo, name ='newtodo'),
        url('edit/(?P<id>\d+)/', views.edit, name ='edit'),
        url('delete/(?P<id>\d+)/', views.delete, name ='delete'),
        
]
