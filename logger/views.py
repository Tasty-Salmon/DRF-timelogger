from django.shortcuts import render
from rest_framework import generics
from .models import EveningLog
from .serializers import LogSerializer

# Create your views here.

class LogList(viewsets.ModelViewSet):
    serializer_class = LogSerializer

class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LogSerializer

    