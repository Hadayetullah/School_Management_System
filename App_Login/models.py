from django.db import models

# To Create a Custom User Model and Admin Panel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy


# To automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


""" A Custom Manager to deal with emails as unique identifier """

class MyUserManager(BaseUserManager):
    """ Creates and saves a user with a given email and password """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(
    gettext_lazy('staff status'),
    default=False,
    help_text = gettext_lazy('Designates whether the user can log in this site')
    )

    is_active = models.BooleanField(
    gettext_lazy('active'),
    default=True,
    help_text = gettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts')
    )

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    # built-in function
    def __str__(self):
        return self.email

    # built-in function
    def get_full_name(self):
        return self.email

    # built-in function
    def get_short_name(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    surname = models.CharField(max_length=200, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=40, blank=True)

    classes = (
    (6, "Class 6"),
    (7, "Class 7"),
    (8, "Class 8"),
    (9, "Class 9"),
    )

    select_class = models.IntegerField(choices=classes, blank=True, null=True)


    department = (
    (1, "Science"),
    (2, "Arts"),
    (3, "Commerce"),
    (4, "Select this option if you want to admit Under class 9"),
    )

    select_department = models.IntegerField(choices=department, blank=True, null=True)

    father_name = models.CharField(max_length=264, blank=True)
    occupation = models.CharField(max_length=300, blank=True)
    mother_name = models.CharField(max_length=264, blank=True)
    village = models.CharField(max_length=300, blank=True)
    post_office = models.CharField(max_length=250, blank=True)
    zipcode = models.IntegerField(default=0, blank=True)
    sub_district = models.CharField(max_length=70, blank=True)
    district = models.CharField(max_length=70, blank=True)
    division = models.CharField(max_length=70, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    present_address = models.TextField(max_length=300, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    admitted = models.BooleanField(default=False)
    roll = models.IntegerField(default=0)
    new_student = models.BooleanField(default=True)
    old_student = models.BooleanField(default=False)
    session = models.IntegerField(default=0)

    # built-in function
    def __str__(self):
        return self.surname + "'s Profile"

    # Not built-in function
    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True

    # Addmission fee
    def admission_fee(self):
        fee = self.select_class
        switcher = {
            6: 600,
            7: 700,
            8: 800,
            9: 900,
        }
        return switcher.get(fee, "0.00")


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
