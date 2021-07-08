from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import OneToOneField
# Create your models here.

class UserData(AbstractUser):

    emp_id = CharField(max_length=10, unique=True)
    mobile_no = CharField(max_length=10)
    group_name = CharField(max_length=7)
    
class Docs(models.Model):
    user = OneToOneField(UserData, primary_key=True, on_delete=models.CASCADE)
    aadhar = BooleanField(default=False)
    pan = BooleanField(default=False)
    passport = BooleanField(default=False)
    d_license = BooleanField(default=False)
