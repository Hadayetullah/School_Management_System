import profile
from rest_framework import serializers
from .models import Profile


class Students(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "full_name", "roll"]