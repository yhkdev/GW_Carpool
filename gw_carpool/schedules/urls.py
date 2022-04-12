from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='schedule'),
    path('<int:schedule_id>', views.schedule, name='schedule'),

    path('schedule_edit', views.schedule_edit, name='schedule_edit'),
    path('schedule_new', views.schedule_new, name='schedule_new'),
]
