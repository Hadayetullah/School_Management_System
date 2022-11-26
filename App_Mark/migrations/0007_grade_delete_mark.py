# Generated by Django 4.1 on 2022-10-12 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Mark', '0006_remove_mark_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.IntegerField(blank=True, default=0, null=True)),
                ('test2', models.IntegerField(blank=True, default=0, null=True)),
                ('test3', models.IntegerField(blank=True, default=0, null=True)),
                ('test4', models.IntegerField(blank=True, default=0, null=True)),
                ('test5', models.IntegerField(blank=True, default=0, null=True)),
                ('test6', models.IntegerField(blank=True, default=0, null=True)),
                ('test7', models.IntegerField(blank=True, default=0, null=True)),
                ('test8', models.IntegerField(blank=True, default=0, null=True)),
                ('test9', models.IntegerField(blank=True, default=0, null=True)),
                ('test10', models.IntegerField(blank=True, default=0, null=True)),
                ('performance1', models.IntegerField(blank=True, default=0, null=True)),
                ('performance2', models.IntegerField(blank=True, default=0, null=True)),
                ('performance3', models.IntegerField(blank=True, default=0, null=True)),
                ('performance4', models.IntegerField(blank=True, default=0, null=True)),
                ('performance5', models.IntegerField(blank=True, default=0, null=True)),
                ('performance6', models.IntegerField(blank=True, default=0, null=True)),
                ('performance7', models.IntegerField(blank=True, default=0, null=True)),
                ('performance8', models.IntegerField(blank=True, default=0, null=True)),
                ('performance9', models.IntegerField(blank=True, default=0, null=True)),
                ('performance10', models.IntegerField(blank=True, default=0, null=True)),
                ('midterm', models.IntegerField(blank=True, default=0, null=True)),
                ('final', models.IntegerField(blank=True, default=0, null=True)),
                ('session', models.IntegerField(verbose_name=2022)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
