from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from accounts.models import Account

# Create your views here.

def signup_user(request):
    if request.method == 'POST':
    # # Don't use django's form method for signup. It messes with css frontend already in place for signup page
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         # phone = form.cleaned_data['phone']
    #         # street_address = form.cleaned_data['street_address']
    #         # city = form.cleaned_data['city']
    #         # state = form.cleaned_data['state']
    #         # zip_code = form.cleaned_data['zip_code']
    #         user = authenticate(request, email=email, password=password)
    #         messages.success(request, 'You have signed up successfully and can now log in')
    #         return redirect('signup_rider')
    # else:
    #     form = CustomUserCreationForm()
    # return render(request, 'accounts/signup_rider.html', {
    #     'form':form,
    # })
        
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
            return redirect('signup_user')
        else:
            # If no problem, signup the rider user
            user = Account.objects.create_user(email=email, password=password,
            first_name=first_name, last_name=last_name, phone=phone, street_address=street_address,
            city=city, state=state, zip_code=zip_code, is_driver=0)
            user.save()
            messages.success(request, 'You have signed up successfully and can log in')
            return redirect('signup_user')
    else:
        return render(request, 'accounts/signup_user.html')

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
