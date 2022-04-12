from django.shortcuts import render

# Create your views here.

# Note: replace 'schedule.html' in index() or schedule() methods at some point!!!  

def index(request):
    return render(request, 'schedules/schedule.html')

def schedule(request):
    return render(request, 'schedules/schedule.html')

def schedule_new(request):
    return render(request, 'schedules/schedule_new.html')
    
def schedule_edit(request):
    return render(request, 'schedules/schedule_edit.html')
