from urllib import response
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello from Web Scrap")
