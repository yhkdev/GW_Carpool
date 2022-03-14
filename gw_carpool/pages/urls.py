from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup_driver', views.signup_driver, name='signup_driver'),
    path('signup_rider', views.signup_rider, name='signup_rider'),
]
