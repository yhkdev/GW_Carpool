from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def signup_rider(request):
    if request.method == 'POST':
        # Get form values
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        street_address = request.POST['street_address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']

        # Check email for duplicate signup
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is already being used')
            return redirect('signup_rider')
        else:
            # If no problem, signup the rider user
            user = User.objects.create_user(email=email, password=password,
            fname=fname, lname=lname, phone=phone, street_address=street_address,
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

def login(request):
    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def myschedule(request):
    return render(request, 'schedules/schedule.html')
