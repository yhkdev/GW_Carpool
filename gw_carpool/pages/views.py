from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('<h1>index page</h1>')
