# Generated by Django 4.0 on 2022-10-14 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0014_profile_session'),
        ('App_Mark', '0013_alter_grade_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Login.profile'),
        ),
    ]
