from django.contrib import admin
from hr_pages.models import Docs, UserData

# Register your models here.

admin.site.register(UserData)
admin.site.register(Docs)