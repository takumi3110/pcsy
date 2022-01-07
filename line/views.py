from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContractNumberViewSet(viewsets.ModelViewSet):
    queryset = ContractNumber.objects.all()
    serializer_class = ContractNumberSerializer


class ParentNumberViewSet(viewsets.ModelViewSet):
    queryset = ParentNumber.objects.all()
    serializer_class = ParentNumberSerializer
