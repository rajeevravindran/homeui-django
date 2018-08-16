# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse


def dashboardHome(request):
    return HttpResponse("Hello")