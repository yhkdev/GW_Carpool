from accounts.models import Account
from django.db import models
from django.urls import reverse

# Use below code to import foreign key db later:
# from users.models import user

# Create your models here.

# Note: Need to somehow bring in django's account user info table in here as 'User'
#       Afterwards, run 'python manage.py makemigrations' & 'python manage.py migrate' to update DB

class Schedule(models.Model):
    
    day_of_the_week = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    destinations = (
        ('Home', 'Home'),
        ('GWU', 'GWU'),
    )

    # owner = models.ForeignKey(Account, on_delete=models.CASCADE)# models.CASCADE = delete all schedule related to the deleted User
    From = models.CharField(max_length=10, choices=destinations)
    to = models.CharField(max_length=10, choices=destinations)
    day = models.CharField(max_length=10, choices=day_of_the_week) # add choices=state_choices to enable dropdown menu in admin area user edit. 
    # But this cause problem getting value from website user registration
    pickup_time = models.TimeField()
    def __str__(self):
        # This is what shows as each row's name when you look from django admin db
        return self.day + " : " + self.From + " to " + self.to

    def get_absolute_url(self):
        return reverse("schedule")
    
