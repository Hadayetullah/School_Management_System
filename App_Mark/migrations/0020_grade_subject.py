# Generated by Django 4.0 on 2022-10-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Mark', '0019_alter_grade_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]