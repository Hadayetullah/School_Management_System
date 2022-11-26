from dataclasses import fields
from rest_framework import serializers
from .models import Attendance
from App_Login.models import Profile


class TakeAttendance(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["id", "user", "student", "class_no", "present", "created", "session"]



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["surname"]