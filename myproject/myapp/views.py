from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
#created a welcome function that will be triggered when we reach out to URL, second paramter if 
# Second parameter is the directory structure as per template/myapp/index.html

def welcome(request):
    return render(request,'myapp/index.html')
