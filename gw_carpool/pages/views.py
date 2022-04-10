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


def event_list(request):
    return render(request, 'pages/event_list.html')


def event_edit(request):
    return render(request, 'pages/event_edit.html')


def event_new(request):
    return render(request, 'pages/event_new.html')


def account_rider(request):
    return render(request, 'pages/account_rider.html')


def account_driver(request):
    return render(request, 'pages/account_driver.html')


def findride(request):
    return render(request, 'pages/findride.html')
