from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Permission
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import os
import psutil

# Getting loadover15 minutes

@api_view(['GET'])
def getload(request):
    load1, load5, load15 = psutil.getloadavg()
    print(psutil.getloadavg(),os.cpu_count(),psutil.cpu_percent(interval=5))
    cpu_usage = (load5 / os.cpu_count()) * 100

    print("The CPU usage is : ", cpu_usage)
    api_urls = {
        'cpu_usage': cpu_usage,
        "cpu_count":os.cpu_count(),
        "cpu_percent":psutil.cpu_percent(interval=1)/os.cpu_count(),
    }
    return JsonResponse(api_urls)