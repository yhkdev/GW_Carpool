from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('signup_user', views.signup_user, name='signup_user'),
    path('findride', views.findride, name='findride'),
    path('profile', views.profile, name='profile'),
]
