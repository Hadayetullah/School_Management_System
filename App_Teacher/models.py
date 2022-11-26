from django.db import models
from App_Login.models import User



# Create your models here.
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    profile_pic = models.ImageField(upload_to='teachers_photo', blank=True)
    surname = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=70, blank=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    id_no = models.IntegerField(default=0)

    subject = (
        ('Bangla 1st paper', 'Bangla 1st paper'),
        ('Bangla 2nd paper', 'Bangla 2nd paper'),
        ('English 1st paper', 'English 1st paper'),
        ('English 2nd paper', 'English 2nd paper'),
        ('Mathematics', 'Mathematics'),
        ('Bangladesh and Global Studies', 'Bangladesh and Global Studies'),
        ('Science', 'Science'),
        ('Information and Communication Technology', 'Information and Communication Technology'),
        ('Islam and Moral Education', 'Islam and Moral Education'),
        ('Hindu Religion and Moral Education', 'Hindu Religion and Moral Education'),
        ('Buddhist Religion and Moral Education', 'Buddhist Religion and Moral Education'),
        ('Christian Religion and Moral Education', 'Christian Religion and Moral Education'),
        ('Agriculture Studies', 'Agriculture Studies'),
        ('Home Science', 'Home Science'),
        ('Higher Mathematics', 'Higher Mathematics'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('Accounting', 'Accounting'),
        ('Finance and Banking', 'Finance and Banking'),
        ('Business Entrepreneurship', 'Business Entrepreneurship'),
        ('Economics', 'Economics'),
        ('Geography', 'Geography'),
        ('History', 'History'),
        ('General Science', 'General Science'),
    )


    subject_1 = models.CharField(max_length=70, choices=subject, blank=True, null=True)
    subject_2 = models.CharField(max_length=70, choices=subject, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=300, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    teacher = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True
