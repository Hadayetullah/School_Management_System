# Generated by Django 4.0 on 2022-07-28 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Login', '0007_rename_address_1_profile_present_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='teachers_photo')),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('full_name', models.CharField(blank=True, max_length=70)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('id_no', models.IntegerField(default=0)),
                ('subject_1', models.CharField(blank=True, choices=[('Bangla 1st paper', 'Bangla 1st paper'), ('Bangla 2nd paper', 'Bangla 2nd paper'), ('English-1st paper', 'English-1st paper'), ('English 2nd paper', 'English 2nd paper'), ('Mathematics', 'Mathematics'), ('Bangladesh and Global Studies', 'Bangladesh and Global Studies'), ('Science', 'Science'), ('Information and Communication Technology', 'Information and Communication Technology'), ('Islam and Moral Education', 'Islam and Moral Education'), ('Hindu Religion and Moral Education', 'Hindu Religion and Moral Education'), ('Buddhist Religion and Moral Education', 'Buddhist Religion and Moral Education'), ('Christian Religion and Moral Education', 'Christian Religion and Moral Education'), ('Agriculture Studies', 'Agriculture Studies'), ('Home Science', 'Home Science'), ('Higher Mathematics', 'Higher Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Accounting', 'Accounting'), ('Finance and Banking', 'Finance and Banking'), ('Business Entrepreneurship', 'Business Entrepreneurship'), ('Economics', 'Economics'), ('Geography', 'Geography'), ('History', 'History'), ('General Science', 'General Science')], max_length=70, null=True)),
                ('subject_2', models.CharField(blank=True, choices=[('Bangla 1st paper', 'Bangla 1st paper'), ('Bangla 2nd paper', 'Bangla 2nd paper'), ('English-1st paper', 'English-1st paper'), ('English 2nd paper', 'English 2nd paper'), ('Mathematics', 'Mathematics'), ('Bangladesh and Global Studies', 'Bangladesh and Global Studies'), ('Science', 'Science'), ('Information and Communication Technology', 'Information and Communication Technology'), ('Islam and Moral Education', 'Islam and Moral Education'), ('Hindu Religion and Moral Education', 'Hindu Religion and Moral Education'), ('Buddhist Religion and Moral Education', 'Buddhist Religion and Moral Education'), ('Christian Religion and Moral Education', 'Christian Religion and Moral Education'), ('Agriculture Studies', 'Agriculture Studies'), ('Home Science', 'Home Science'), ('Higher Mathematics', 'Higher Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Accounting', 'Accounting'), ('Finance and Banking', 'Finance and Banking'), ('Business Entrepreneurship', 'Business Entrepreneurship'), ('Economics', 'Economics'), ('Geography', 'Geography'), ('History', 'History'), ('General Science', 'General Science')], max_length=70, null=True)),
                ('religion', models.CharField(blank=True, max_length=30)),
                ('phone_no', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True, max_length=300)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('teacher', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='App_Login.user')),
            ],
        ),
    ]
