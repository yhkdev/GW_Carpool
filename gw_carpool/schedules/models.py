from django.db import models

# Use below code to import foreign key db later:
# from users.models import user

# Create your models here.

# Note: Need to somehow bring in django's account user info table in here as 'User'
#       Afterwards, run 'python manage.py makemigrations' & 'python manage.py migrate' to update DB

class Schedule(models.Model):
    #user: models.ForeignKey(User, on_delete=models.CASCADE) # models.CASCADE = delete all schedule related to the deleted User
    From = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    date = models.DateField()
    pickup_time = models.TimeField()
    def __str__(self):
        # This is what shows as each row's name when you look from django admin db
        return self.From + " to " + self.to
