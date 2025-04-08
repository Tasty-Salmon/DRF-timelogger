from django import forms
from .models import EveningLog
from datetime import datetime, timedelta

class EveningLogForm(forms.ModelForm):
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
        widgets = {
            'start': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-input mt-2'
            }),
            'end': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-input mt-2'
            }),
        }