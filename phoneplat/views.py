from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .serializer import *
from .models import *
from .filter import *


# Create your views here.
class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    filter_class = TenantFilter


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_class = TeamFilter


class DeptViewSet(viewsets.ModelViewSet):
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    filter_class = DeptFilter


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class LineCategoryViewSet(viewsets.ModelViewSet):
    queryset = LineCategory.objects.all()
    serializer_class = LineCategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ContractNumberViewSet(viewsets.ModelViewSet):
    queryset = ContractNumber.objects.all()
    serializer_class = ContractNumberSerializer


class ParentNumberViewSet(viewsets.ModelViewSet):
    queryset = ParentNumber.objects.all()
    serializer_class = ParentNumberSerializer


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
