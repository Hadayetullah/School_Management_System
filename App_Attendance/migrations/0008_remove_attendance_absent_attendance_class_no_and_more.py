# Generated by Django 4.1 on 2022-09-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Attendance', '0007_alter_attendance_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='absent',
        ),
        migrations.AddField(
            model_name='attendance',
            name='class_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='session',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
