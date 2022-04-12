from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class NewUser(models.Model):
    #user: models.ForeignKey(User, on_delete=models.CASCADE) # models.CASCADE = delete all schedule related to the deleted User
    email: models.CharField(max_length=100)
    first_name: models.CharField(max_length=100)
    last_name: models.CharField(max_length=100)
    is_superuser: models.BooleanField(default=False)
    is_staff: models.BooleanField(default=False)
    is_active: models.BooleanField(default=False)
    def __str__(self):
        # This is what shows as each row's name when you look from django admin db
        return self.first_name + " " + self.last_name
