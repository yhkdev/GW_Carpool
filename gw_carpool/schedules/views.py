from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ScheduleForm
from .models import Schedule

# Create your views here.

class ScheduleView(ListView):
    model = Schedule
    template_name = 'schedule.html'
    # ordering = ['day']

class ScheduleAddView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedules/schedule_new.html'
    # fields = '__all__'

class ScheduleEditView(UpdateView):
    model = Schedule
    template_name = 'schedules/schedule_edit.html'
    form_class = ScheduleForm

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedules/schedule_delete.html'

    # Below doesn't work if you want to reverse to a view/url with variable (i.e. <int:pk>)
    # success_url = lazy_reverse("schedule")

    # Use this to pass owner_id to urls for DeleteView
    # Source: https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.DeletionMixin.success_url
    success_url = "/schedules/{owner_id}"
