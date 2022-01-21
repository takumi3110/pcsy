from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from rest_framework import viewsets

from .serializers import *
from .models import *
from .filters import *


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    filter_class = SystemFilter


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    filter_class = PhoneNumberFilter


class SurplusNumberViewSet(viewsets.ModelViewSet):
    queryset = SurplusNumber.objects.all()
    serializer_class = SurplusNumberSerializer
    filter_class = SurplusNumberFilter


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_class = ServiceFilter


class AccessLineViewSet(viewsets.ModelViewSet):
    queryset = AccessLine.objects.all()
    serializer_class = AccessLineSerializer
    filter_class = AccessLineFilter


class TrankViewSet(viewsets.ModelViewSet):
    queryset = Trank.objects.all()
    serializer_class = TrankSerializer
    filter_class = TrankFilter


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
    filter_class = ScenarioFilter


class TrankInfoViewSet(viewsets.ModelViewSet):
    queryset = TrankInfo.objects.all()
    serializer_class = TrankInfoSerializer
    filter_class = TrankInfoFilter


class PayingServiceViewSet(viewsets.ModelViewSet):
    queryset = PayingService.objects.all()
    serializer_class = PayingServiceSerializer
    filter_class = PayingServiceFilter


class IncomingNumberViewSet(viewsets.ModelViewSet):
    queryset = IncomingNumber.objects.all()
    serializer_class = IncomingNumberSerializer
    filter_class = IncomingNumberFilter


class PayingCodeViewSet(viewsets.ModelViewSet):
    queryset = PayingCode.objects.all()
    serializer_class = PayingCodeSerializer
    filter_class = PayingCodeFilter


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_class = NotificationFilter


def index(request):
    return render(request, 'phonePlat/index.html')


class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'phonePlat/index.html'
    paginate_by = 20
