from django.shortcuts import render
from django.http import HttpResponse




def post_list(request):
    return HttpResponse("<h1> Hello Worlsd</h1>")