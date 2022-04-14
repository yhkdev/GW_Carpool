from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('signup_rider', views.signup_rider, name='signup_rider'),
    path('signup_driver', views.signup_driver, name='signup_driver'),
]
