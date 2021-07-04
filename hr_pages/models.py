from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.fields import CharField, UUIDField
# Create your models here.

class UserData(AbstractUser):

    emp_id = CharField(max_length=10)
    mobile_no = CharField(max_length=10)
    
