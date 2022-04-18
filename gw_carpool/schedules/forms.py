from tkinter import HIDDEN

from django import forms

from .models import Schedule


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('From', 'to', 'day', 'pickup_time')

        widgets = {
            'From': forms.Select(attrs={'class': 'form-control mt-1'}),
            'to': forms.Select(attrs={'class': 'form-control mt-1'}),
            'day': forms.Select(attrs={'class': 'form-control mt-1'}),
            'pickup_time': forms.TimeInput(attrs={'class': 'form-control mt-1', 'type': 'time'}),
        }
