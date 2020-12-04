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

from .serializers import CompanyViewSerializer
from .models import Company

# Create your views here.

class CompanyView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        company = request.user.company
        get_object_or_404(Company, id=company.id)
        serializer = CompanyViewSerializer(company)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['owner'] = request.user.id
        serializer = CompanyViewSerializer(data=data)
        if serializer.is_valid():
            company = serializer.save(owner=request.user)
            request.user.company = company 
            request.user.save()
            return Response(serializer.data)
        return Response(serializer.errors)