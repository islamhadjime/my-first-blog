
from django.urls import path
from .views import *

urlpatterns  = [
    path('', post_list, name='post_list'),
    path('about/',about,name = 'about'),


    path('python/',python,name = 'python'),
    path('linux/',linux,name = 'linux'),
    path('cshat/',cshat,name = 'cshat'),
]
