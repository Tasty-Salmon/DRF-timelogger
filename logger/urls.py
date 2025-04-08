
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserDetail, UserList, LogList, LogCreateView, LogDayView

urlpatterns = [
    path("users/", UserList.as_view()),  
    path("users/<int:pk>/", UserDetail.as_view()),  
    path("create/",LogCreateView.as_view(), name = 'log-create'),
    path("", LogList.as_view(), name = 'log-list'),
    path("date/", LogDayView.as_view(), name = 'LogDayView'),
 ]