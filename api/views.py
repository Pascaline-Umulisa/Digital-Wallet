from django.shortcuts import render
from rest_framework import viewsets
from wallet import models
from .serializer import CustomerSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=models.Customer.objects.all()
    serializer_class=CustomerSerializer