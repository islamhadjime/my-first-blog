
from django.urls import path
from .views import *

urlpatterns  = [
    path('', post_list, name='post_list'),
    path('about/',about,name = 'about')
]
