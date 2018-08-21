# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import AlarmEventSerializer
from .models import AlarmEvent
# Create your views here.

class ListAlarmsView(generics.ListAPIView):
    queryset = AlarmEvent.objects.all()
    print queryset
    serializer_class = AlarmEventSerializer
