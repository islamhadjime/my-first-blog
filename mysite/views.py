from django.shortcuts import render
#from django.http import HttpResponse
from .models import *



def post_list(request):
    return  render(request , 'mysite/index.html')

def about(request):
    return render(request , 'mysite/about.html')
