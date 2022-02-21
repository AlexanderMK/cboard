from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Meetings(models.Model):
   title = models.CharField(max_length=100)
   time = models.DateTimeField()
   location = models.CharField(max_length=100)


class Participant(models.Model):
    firstName = models.CharField(max_length = 100)
    middleName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here