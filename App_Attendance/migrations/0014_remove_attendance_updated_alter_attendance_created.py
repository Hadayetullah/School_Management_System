# Generated by Django 4.1 on 2022-10-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Attendance', '0013_alter_attendance_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='updated',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
