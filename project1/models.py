from django.db.models.fields.related import ForeignKey
from hr_pages.models import UserData
from django.db import models
from django.db.models.fields import CharField, DateField, TimeField
from hr_pages.models import UserData

# Create your models here.

class Notifications(models.Model):
    user = ForeignKey(UserData, on_delete=models.CASCADE)
    title = CharField(max_length=255)
    notification = CharField(max_length=255)
    date = DateField(auto_now_add=True)
    time = TimeField(auto_now_add=True)

class Schedule(models.Model):
    title = CharField(max_length=255)
    date = DateField()
    time = TimeField(max_length=20)
    group = CharField(max_length=10)
    description = CharField(max_length=255, default=None, blank=True, null=True)