# Generated by Django 4.0 on 2022-08-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Teacher', '0006_alter_teacher_subject_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject_1',
            field=models.CharField(blank=True, choices=[(1, 'Bangla 1st paper'), (2, 'Bangla 2nd paper'), (3, 'English-1st paper'), (3, 'English 2nd paper'), (4, 'Mathematics')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject_2',
            field=models.CharField(blank=True, choices=[(1, 'Bangla 1st paper'), (2, 'Bangla 2nd paper'), (3, 'English-1st paper'), (3, 'English 2nd paper'), (4, 'Mathematics')], default=4, max_length=70, null=True),
        ),
    ]
