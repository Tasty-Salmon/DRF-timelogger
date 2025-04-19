from django.db import models
from django.conf import settings

# Create your models here.

class EveningLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete= models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    activity = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    