from dataclasses import fields
from rest_framework import serializers
from .models import Grade


class SubmitGrade(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'