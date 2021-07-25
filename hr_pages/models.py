from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import OneToOneField
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class UserData(AbstractUser):

    emp_id = CharField(max_length=10, unique=True)
    mobile_no = CharField(max_length=10)
    group_name = CharField(max_length=7)
    prof_pic = models.ImageField(upload_to=user_directory_path, default=None, blank=True, null=True)
    
class Docs(models.Model):
    user = OneToOneField(UserData, primary_key=True, on_delete=models.CASCADE)
    aadhar_card = BooleanField(default=False)
    pan_card = BooleanField(default=False)
    passport = BooleanField(default=False)
    driving_license = BooleanField(default=False)
