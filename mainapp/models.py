from django.db import models
from django.contrib.auth.models import User

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,unique=True)