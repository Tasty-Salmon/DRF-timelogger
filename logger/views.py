from django.shortcuts import render
from rest_framework import generics
from .models import EveningLog
from .serializers import LogSerializer, UserSerializer
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.urls import reverse_lazy
from .models import EveningLog
from .forms import EveningLogForm
from datetime import datetime, date
from collections import defaultdict



# Create your views here.

class LogList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    queryset = EveningLog.objects.all().order_by('-start')
    serializer_class = LogSerializer
    
    
    def get(self,request):
        logs = self.get_queryset()
        grouped_logs = defaultdict(list)

        for log in logs:
            print("log:", log, "start:", log.start)
            date = log.start.date()
            grouped_logs[date].append(log)

        grouped_logs = dict(sorted(grouped_logs.items(), reverse=True))

        serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response({'grouped_logs': grouped_logs, 'serialized': serializer.data}, template_name='list.html')

class LogDayView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = LogSerializer
    
    def get_queryset(self):
        date_param = self.request.GET.get('date')
        if date_param:
            return EveningLog.objects.filter(start__date=date_param)
        return EveningLog.objects.none()  

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response({'items': queryset}, template_name = 'DayList.html')


class LogCreateView(CreateView):
    model = EveningLog
    form_class = EveningLogForm
    template_name = 'log_create.html'
    success_url = reverse_lazy('log-list')



class LogEditView(UpdateView):
    model = EveningLog
    form_class = EveningLogForm
    template_name = 'log_create.html'
    success_url = reverse_lazy('log-list')


class UserList(generics.ListCreateAPIView):  
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):  
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer