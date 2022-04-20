from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ScheduleForm
from .models import Account, Schedule

# Create your views here.

# Journal == Account
# Article == Schedule 

class ScheduleView(ListView):
    model = Schedule
    template_name = 'schedule.html'
    # ordering = ['day']

    def get_context_data(self,*args, **kwargs):
        """ Get Account obj (the schedule owner) using 'owner_id' path passed from urls.py as fk. Pass it on to schedule_list.html 
            Used to compare schedule owner with currently logged-in user to hide the create, edit, delete schedule buttons. 
            "self.kwargs['owner_id']" is used to get the path as a variable. 
        """
        context = super(ScheduleView, self).get_context_data(*args,**kwargs)
        context['owner_obj'] = get_object_or_404(Account, pk=self.kwargs['owner_id'])
        return context
        
    def get_queryset(self):
        """ Filter schedule items to be displayed in schedule_list.html by its schedule owner (using 'owner_id' path passed from urls.py) """
        return Schedule.objects.filter(owner=self.kwargs['owner_id'])



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
