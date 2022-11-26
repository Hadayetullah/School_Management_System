# Generated by Django 4.0 on 2022-07-03 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log in this site', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('full_name', models.CharField(blank=True, max_length=264)),
                ('dob', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10)),
                ('father_name', models.CharField(blank=True, max_length=264)),
                ('occupation', models.CharField(blank=True, max_length=300)),
                ('mother_name', models.CharField(blank=True, max_length=264)),
                ('village', models.CharField(blank=True, max_length=300)),
                ('post_office', models.CharField(blank=True, max_length=250)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('sub_district', models.CharField(blank=True, max_length=70)),
                ('district', models.CharField(blank=True, max_length=70)),
                ('division', models.CharField(blank=True, max_length=70)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('address_1', models.TextField(blank=True, max_length=300)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('admitted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='App_Login.user')),
            ],
        ),
    ]