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


def schedule(request):
    return render(request, 'pages/schedule.html')


def schedule_edit(request):
    return render(request, 'pages/schedule_edit.html')


def schedule_new(request):
    return render(request, 'pages/schedule_new.html')


def account_rider(request):
    return render(request, 'pages/account_rider.html')


def account_driver(request):
    return render(request, 'pages/account_driver.html')


def findride(request):
    return render(request, 'pages/findride.html')
