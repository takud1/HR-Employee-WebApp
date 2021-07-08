# Generated by Django 3.2.4 on 2021-07-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_pages', '0002_auto_20210705_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hr_pages.userdata')),
                ('aadhar', models.BooleanField(default=False)),
                ('pan', models.BooleanField(default=False)),
                ('passport', models.BooleanField(default=False)),
                ('d_license', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='emp_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
