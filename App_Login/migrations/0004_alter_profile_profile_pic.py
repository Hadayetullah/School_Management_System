# Generated by Django 4.0 on 2022-07-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_profile_gender_profile_religion_profile_select_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
