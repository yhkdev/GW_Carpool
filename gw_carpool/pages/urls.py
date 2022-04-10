from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup_driver', views.signup_driver, name='signup_driver'),
    path('signup_rider', views.signup_rider, name='signup_rider'),
    path('event_list', views.event_list, name='event_list'),
    path('event_edit', views.event_edit, name='event_edit'),
    path('event_new', views.event_new, name='event_new'),
    path('account_rider', views.account_rider, name='account_rider'),
    path('account_driver', views.account_driver, name='account_driver'),
    path('findride', views.findride, name='findride'),
]
