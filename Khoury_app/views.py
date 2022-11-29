from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .serializers import DepartmentSerializer
from . import models


# Create your views here.
class DepartmentList(generics.ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = DepartmentSerializer
