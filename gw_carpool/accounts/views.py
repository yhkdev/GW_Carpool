from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.models import Account

# Create your views here.

def signup_rider(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        street_address = request.POST['street_address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']

        # Check email for duplicate signup
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'That email is already being used')
            return redirect('signup_rider')
        else:
            # If no problem, signup the rider user
            user = Account.objects.create_user(email=email, password=password,
            first_name=first_name, last_name=last_name, phone=phone, street_address=street_address,
            city=city, state=state, zip_code=zip_code, is_driver=0)
            user.save()
            messages.success(request, 'You have signed up successfully and can log in')
            return redirect('register')
    else:
        return render(request, 'accounts/signup_rider.html')

def signup_driver(request):
    if request.method == 'POST':
        # Signup Driver
        return
    else:
        return render(request, 'accounts/signup_driver.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid email and/or password')
            return render(request, 'accounts/login_user.html')
    else:
        return render(request, 'accounts/login_user.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Logged Out')
    return redirect('index')

# def myschedule(request):
#     return render(request, 'schedules/schedule.html')
