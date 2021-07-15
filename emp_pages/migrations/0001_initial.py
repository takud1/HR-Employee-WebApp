# Generated by Django 3.2.4 on 2021-07-13 06:15

from django.db import migrations, models
import django.db.models.deletion
import emp_pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Up_Docs',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hr_pages.userdata')),
                ('aadhar_f', models.FileField(blank=True, default=None, null=True, upload_to=emp_pages.models.user_directory_path)),
                ('pan_f', models.FileField(blank=True, default=None, null=True, upload_to=emp_pages.models.user_directory_path)),
                ('passport_f', models.FileField(blank=True, default=None, null=True, upload_to=emp_pages.models.user_directory_path)),
                ('d_license_f', models.FileField(blank=True, default=None, null=True, upload_to=emp_pages.models.user_directory_path)),
            ],
        ),
    ]
