from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from .models import Student

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer