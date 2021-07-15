from django.db import models
from hr_pages.models import UserData
from django.db.models.fields.related import OneToOneField

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Up_Docs(models.Model):
    user = OneToOneField(UserData, primary_key=True, on_delete=models.CASCADE)
    aadhar_f = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    pan_f = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    passport_f = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    d_license_f = models.FileField(upload_to=user_directory_path, blank=True, null=True)