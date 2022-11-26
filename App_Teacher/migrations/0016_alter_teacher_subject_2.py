# Generated by Django 4.0 on 2022-08-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Teacher', '0015_alter_teacher_subject_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject_2',
            field=models.CharField(choices=[('Bangla 1st paper', 'Bangla 1st paper'), ('Bangla 2nd paper', 'Bangla 2nd paper'), ('English-1st paper', 'English-1st paper'), ('English 2nd paper', 'English 2nd paper'), ('Mathematics', 'Mathematics'), ('Bangladesh and Global Studies', 'Bangladesh and Global Studies'), ('Science', 'Science'), ('Information and Communication Technology', 'Information and Communication Technology'), ('Islam and Moral Education', 'Islam and Moral Education'), ('Hindu Religion and Moral Education', 'Hindu Religion and Moral Education'), ('Buddhist Religion and Moral Education', 'Buddhist Religion and Moral Education'), ('Christian Religion and Moral Education', 'Christian Religion and Moral Education'), ('Agriculture Studies', 'Agriculture Studies'), ('Home Science', 'Home Science'), ('Higher Mathematics', 'Higher Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Accounting', 'Accounting'), ('Finance and Banking', 'Finance and Banking'), ('Business Entrepreneurship', 'Business Entrepreneurship'), ('Economics', 'Economics'), ('Geography', 'Geography'), ('History', 'History'), ('General Science', 'General Science'), ('x', 'Do not have second subject')], default='a', max_length=70),
        ),
    ]
