from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup_driver', views.signup_driver, name='signup_driver'),
    path('signup_rider', views.signup_rider, name='signup_rider'),
    path('schedule', views.schedule, name='schedule'),
    path('schedule_edit', views.schedule_edit, name='schedule_edit'),
    path('schedule_new', views.schedule_new, name='schedule_new'),
    path('account_rider', views.account_rider, name='account_rider'),
    path('account_driver', views.account_driver, name='account_driver'),
    path('findride', views.findride, name='findride'),
]
