from django.shortcuts import render
#from django.http import HttpResponse
from .models import *



def post_list(request):
    return  render(request , 'mysite/index.html')

def about(request):
    return render(request , 'mysite/about.html')


def python(request):
    return render(request , 'mysite/python.html')

def linux(request):
    return render(request , 'mysite/linux.html')


def cshat(request):
    return render(request , 'mysite/cshat.html')
