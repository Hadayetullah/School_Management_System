# Generated by Django 4.1 on 2022-09-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Attendance', '0002_attendance_created_attendance_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name_plural': 'Attendance'},
        ),
        migrations.AlterField(
            model_name='attendance',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]