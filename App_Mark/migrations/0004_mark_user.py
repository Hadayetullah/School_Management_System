# Generated by Django 4.1 on 2022-10-12 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0014_profile_session'),
        ('App_Mark', '0003_remove_mark_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App_Login.profile'),
            preserve_default=False,
        ),
    ]
