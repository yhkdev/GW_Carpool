from django.urls import path

from . import views
from .views import ScheduleAddView, ScheduleEditView, ScheduleView

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('schedule_new', ScheduleAddView.as_view(), name='schedule_new'),
    path('<int:pk>', ScheduleEditView.as_view(), name='schedule_edit'),
]
