from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account_rider', views.account_rider, name='account_rider'),
    path('account_driver', views.account_driver, name='account_driver'),
    path('findride', views.findride, name='findride'),
]
