# Generated by Django 4.0 on 2022-10-14 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0014_profile_session'),
        ('App_Mark', '0012_alter_grade_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App_Login.profile'),
        ),
    ]
