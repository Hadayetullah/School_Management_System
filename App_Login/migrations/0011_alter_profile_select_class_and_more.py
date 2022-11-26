# Generated by Django 4.0 on 2022-08-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0010_alter_profile_select_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='select_class',
            field=models.IntegerField(blank=True, choices=[(6, 'Class 6'), (7, 'Class 7'), (8, 'Class 8'), (9, 'Class 9')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='select_department',
            field=models.IntegerField(blank=True, choices=[(1, 'Science'), (2, 'Arts'), (3, 'Commerce'), (4, 'Under class 9')], null=True),
        ),
    ]
