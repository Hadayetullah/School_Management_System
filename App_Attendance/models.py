from django.db import models
from datetime import datetime


# Models
from App_Login.models import User, Profile
from App_Teacher.models import Teacher


# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='take_attendance')
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attend')
    class_no = models.IntegerField(default=0)
    present = models.BooleanField(default=False)
    created = models.DateField(blank=True, null=True)
    session = models.IntegerField(default=0)

    def __str__(self):
        return self.student.surname

    class Meta:
        verbose_name_plural = "Attendance"
