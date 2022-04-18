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
    success_url = reverse_lazy('schedule')


# Note: replace 'schedule.html' in index() or schedule() methods at some point!!!  

# def index(request):
#     user_schedules = Schedule.objects.all()

#     context = {
#         'schedules': user_schedules
#     }

#     return render(request, 'schedules/schedule.html', context)


# def schedule(request):
#     # user_accounts = Account.objects.all()

#     # Craete accounts object, and define'accounts.full_name' to be used in html jinja
#     user_schedules = Schedule

#     context = {
#         'schedules': user_schedules
#     }

#     return render(request, 'schedules/schedule.html', context)


# def schedule_new(request):
#     return render(request, 'schedules/schedule_new.html')
    
# def schedule_edit(request):
#     return render(request, 'schedules/schedule_edit.html')


