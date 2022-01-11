from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .serializers import *
from .models import *
from .filters import *


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class SurplusNumberViewSet(viewsets.ModelViewSet):
    queryset = SurplusNumber.objects.all()
    serializer_class = SurplusNumberSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_class = ServiceFilter


class AccessLineViewSet(viewsets.ModelViewSet):
    queryset = AccessLine.objects.all()
    serializer_class = AccessLineSerializer


class TrankViewSet(viewsets.ModelViewSet):
    queryset = Trank.objects.all()
    serializer_class = TrankSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
    filter_class = ScenarioFilter


class TrankInfoViewSet(viewsets.ModelViewSet):
    queryset = TrankInfo.objects.all()
    serializer_class = TrankInfoSerializer


class PayingServiceViewSet(viewsets.ModelViewSet):
    queryset = PayingService.objects.all()
    serializer_class = PayingServiceSerializer


class IncomingNumberViewSet(viewsets.ModelViewSet):
    queryset = IncomingNumber.objects.all()
    serializer_class = IncomingNumberSerializer


class PayingCodeViewSet(viewsets.ModelViewSet):
    queryset = PayingCode.objects.all()
    serializer_class = PayingCodeSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
