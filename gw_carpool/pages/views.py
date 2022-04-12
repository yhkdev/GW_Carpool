from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def account_rider(request):
    return render(request, 'pages/account_rider.html')


def account_driver(request):
    return render(request, 'pages/account_driver.html')


def findride(request):
    return render(request, 'pages/findride.html')
