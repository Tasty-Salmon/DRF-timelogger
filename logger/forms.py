from django import forms
from .models import EveningLog
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


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

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')
        user = cleaned_data.get('user')

        overlapping = EveningLog.objects.filter(
        user=user,
        start__lt=end,
        end__gt=start,
        )

        if self.instance.pk:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise ValidationError("This time range overlaps with another log.")

        return cleaned_data