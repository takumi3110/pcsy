from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *
from .filters import *


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    filter_class = CareerFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_class = CategoryFilter


class ContractNumberViewSet(viewsets.ModelViewSet):
    queryset = ContractNumber.objects.all()
    serializer_class = ContractNumberSerializer
    filter_class = ContractNumberFilter


class ParentNumberViewSet(viewsets.ModelViewSet):
    queryset = ParentNumber.objects.all()
    serializer_class = ParentNumberSerializer
    filter_class = ParentNumberFilter
