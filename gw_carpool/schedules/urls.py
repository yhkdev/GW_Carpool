from django.urls import path

from . import views
from .views import (ScheduleAddView, ScheduleDeleteView, ScheduleEditView,
                    ScheduleView)

urlpatterns = [
    path('<int:owner_id>', ScheduleView.as_view(), name='schedule'),
    path('schedule_new', ScheduleAddView.as_view(), name='schedule_new'),
    path('edit/<int:pk>', ScheduleEditView.as_view(), name='schedule_edit'),
    path('delete/<int:pk>', ScheduleDeleteView.as_view(), name='schedule_delete'),
]
