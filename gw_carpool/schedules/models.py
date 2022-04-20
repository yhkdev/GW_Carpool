from accounts.models import Account
from crum import get_current_user
from django.db import models
from django.urls import reverse

# "crum": 'django-crum' pkg installed through pip. Imported to Middleware in settings.py. Used to get currently logged-in user obj in django

# Create your models here.

# Note: Need to somehow bring in django's account user info table in here as 'User'
#       Afterwards, run 'python manage.py makemigrations' & 'python manage.py migrate' to update DB

class Schedule(models.Model):
    
    # day_of_the_week = (
    #     ('1', 'Monday'),
    #     ('2', 'Tuesday'),
    #     ('3', 'Wednesday'),
    #     ('4', 'Thursday'),
    #     ('5', 'Friday'),
    #     ('6', 'Saturday'),
    #     ('7', 'Sunday'),
    # )

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

    owner = models.ForeignKey(Account, on_delete=models.CASCADE, default=get_current_user) # models.CASCADE = delete all schedule related to the deleted User
    From = models.CharField(max_length=10, choices=destinations)
    to = models.CharField(max_length=10, choices=destinations)
    day = models.CharField(max_length=10, choices=day_of_the_week) # add choices=state_choices to enable dropdown menu in admin area user edit.
    pickup_time = models.TimeField()

    def __str__(self):
        # This is what shows as each row's name when you look from django admin db
        return self.day + " : " + self.From + " to " + self.to

    def get_absolute_url(self):
        return reverse("schedule", kwargs={"pk": self.owner})
    
