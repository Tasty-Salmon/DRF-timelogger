from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import EveningLog

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "activity",
            "start",
            "end",
            "notes",
        )
        model = EveningLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username',)