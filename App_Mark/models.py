
from email.policy import default
from pyexpat import model
from django.db import models
from App_Login.models import User
# from django.conf import settings


from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    full_name = models.TextField(blank=True, null=True)
    class_no = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    roll = models.IntegerField(default=0)
    test1 = models.IntegerField(default=0)
    test2 = models.IntegerField(default=0)
    test3 = models.IntegerField(default=0)
    test4 = models.IntegerField(default=0)
    test5 = models.IntegerField(default=0)
    test6 = models.IntegerField(default=0)
    test7 = models.IntegerField(default=0)
    test8 = models.IntegerField(default=0)
    test9 = models.IntegerField(default=0)
    test10 = models.IntegerField(default=0)
    performance1 = models.IntegerField(default=0)
    performance2 = models.IntegerField(default=0)
    performance3 = models.IntegerField(default=0)
    performance4 = models.IntegerField(default=0)
    performance5 = models.IntegerField(default=0)
    performance6 = models.IntegerField(default=0)
    performance7 = models.IntegerField(default=0)
    performance8 = models.IntegerField(default=0)
    performance9 = models.IntegerField(default=0)
    performance10 = models.IntegerField(default=0)
    midterm = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    session = models.IntegerField(default=0)
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email

