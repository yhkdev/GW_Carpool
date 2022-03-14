from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def signup_driver(request):
    return render(request, 'pages/signup_driver.html')


def signup_rider(request):
    return render(request, 'pages/signup_rider.html')
