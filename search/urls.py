from django.urls import path, re_path

from . import views

import re



urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(.*)/$', views.info, name='info'),
    
]