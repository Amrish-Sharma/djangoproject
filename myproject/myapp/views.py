from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def welcome(reqest):
    #return hr('Hello')
    return hr('<h1>Hi,Amrish</h1>')
