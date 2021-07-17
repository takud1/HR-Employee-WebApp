from django.db import models
from django.db.models.fields import CharField
from hr_pages.models import UserData
from django.db.models.fields.related import OneToOneField

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Up_Docs(models.Model):
    user = OneToOneField(UserData, primary_key=True, on_delete=models.CASCADE)
    aadhar_card = models.FileField(upload_to=user_directory_path, default=None, blank=True, null=True)
    pan_card = models.FileField(upload_to=user_directory_path, default=None, blank=True, null=True)
    passport = models.FileField(upload_to=user_directory_path, default=None, blank=True, null=True)
    driving_license = models.FileField(upload_to=user_directory_path, default=None, blank=True, null=True)
    aadhar_status = CharField(max_length=15, default="Processing")
    pan_status = CharField(max_length=15, default="Processing")
    passport_status = CharField(max_length=15, default="Processing")
    driving_status = CharField(max_length=15, default="Processing")
