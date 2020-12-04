from django.shortcuts import render

# Django package
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
# DRF package
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskViewSerializer
from .models import Task

# Create your views here.

class TaskView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.data.get('id', None)
        tasks = Task.objects.filter(id=id).all()
        serializer = TaskViewSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = TaskViewSerializer(data=data)
        if serializer.is_valid():
            serializer.save(assignee=request.user, company=request.user.company)
            return Response(serializer.data)
        return Response(serializer.errors)