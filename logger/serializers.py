from rest_framework import serializers

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