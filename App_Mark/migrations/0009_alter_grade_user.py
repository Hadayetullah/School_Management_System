# Generated by Django 4.1 on 2022-10-12 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0014_profile_session'),
        ('App_Mark', '0008_grade_updated_alter_grade_final_alter_grade_midterm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App_Login.profile'),
        ),
    ]
