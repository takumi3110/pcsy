from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView
from django_filters.views import FilterView
from django.db.models import Q

from rest_framework import viewsets

from .serializers import *
from .models import *
from .filters import *
from .forms import *


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


@login_required()
def index(request):
	link_list = {
		'site': 'サイト',
		'tenant': 'テナント',
		'team': 'チーム',
		'service': 'サービス',
		'scenario': 'シナリオ',
		'phone': '電話番号',
		'incoming': '着信課金番号',
		'paying': '課金番号',
		'access': 'アクセス回線',
	}
	return render(request, 'index.html', {'link_list': link_list})


class ServiceListView(LoginRequiredMixin, ListView):
	model = Service
	template_name = 'phonePlat/service/service_list.html'
	paginate_by = 30
	ordering = '-number'

	def get_queryset(self):
		"""
		get_query = self.request.GET.get('q', None).split(' ')
		for query in get_query:
			lookups = (
				Q(number__icontains=query) |
				Q(name__icontains=query) |
				Q(team__name__icontains=query)
			)
		"""
		query = self.request.GET.get('q', None)
		lookups = (
				Q(number__icontains=query) |
				Q(name__icontains=query) |
				Q(team__name__icontains=query)
		)
		if query is not None:
			queryset = super().get_queryset().filter(lookups).distinct().order_by('number')
		else:
			queryset = super().get_queryset().order_by('number')
		return queryset


class ServiceDetailView(LoginRequiredMixin, DetailView):
	model = Service
	template_name = 'phonePlat/service/service_detail.html'


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
	model = Service
	template_name = 'phonePlat/service/service_update.html'
	form_class = CrispyServiceUpdateForm


class ScenarioListView(LoginRequiredMixin, ListView):
	model = Scenario
	template_name = 'phonePlat/scenario/scenario_list.html'
	paginate_by = 30

	def get_queryset(self):
		"""
		get_query = self.request.GET.get('q', None).split(' ')
		for query in get_query:
			lookups = (
				Q(number__icontains=query) |
				Q(name__icontains=query) |
				Q(team__name__icontains=query)
			)
		"""
		query = self.request.GET.get('q', None)
		lookups = (
				Q(number__icontains=query) |
				Q(name__icontains=query) |
				Q(team__name__icontains=query) |
				Q(service__name__icontains=query)
		)
		if query is not None:
			queryset = super().get_queryset().filter(lookups).distinct().order_by('number')
		else:
			queryset = super().get_queryset().order_by('number')
		return queryset


class ScenarioDetailView(LoginRequiredMixin, DetailView):
	model = Scenario
	template_name = 'phonePlat/scenario/scenario_detail.html'


class ScenarioUpdateView(LoginRequiredMixin, UpdateView):
	model = Scenario
	template_name = 'phonePlat/scenario/scenario_update.html'
	form_class = CrispyScenarioUpdateForm


class PhoneNumberListView(LoginRequiredMixin, ListView):
	model = PhoneNumber
	template_name = 'phonePlat/phone_number/phone_number_list.html'
	paginate_by = 30

	def get_queryset(self):
		query = self.request.GET.get('q', None)
		lookups = (
			Q(number__icontains=query) |
			Q(parent_number__number__icontains=query) |
			Q(service__name__icontains=query) |
			Q(ticket=query)
		)
		if query is not None:
			queryset = super().get_queryset().filter(lookups).distinct().order_by('number')
		else:
			queryset = super().get_queryset().order_by('number')
		return queryset


class PhoneNumberDetailView(LoginRequiredMixin, DetailView):
	model = PhoneNumber
	template_name = 'phonePlat/phone_number/phone_number_detail.html'


class PhoneNumberUpdateView(LoginRequiredMixin, UpdateView):
	model = PhoneNumber
	template_name = 'phonePlat/phone_number/phone_number_update.html'
	form_class = CrispyPhoneNumberUpdateForm


class IncomingNumberListView(LoginRequiredMixin, ListView):
	model = IncomingNumber
	template_name = 'phonePlat/incoming_number/list.html'
	paginate_by = 30

	def get_queryset(self):
		query = self.request.GET.get('q', None)
		lookups = (
			Q(number__icontains=query) |
			Q(target_did__icontains=query) |
			Q(service__name__icontains=query) |
			Q(paying_service__name__icontains=query)
		)
		if query is not None:
			queryset = super().get_queryset().filter(lookups).distinct().order_by('number')
		else:
			queryset = super().get_queryset().order_by('number')
		return queryset


class IncomingNumberDetailView(LoginRequiredMixin, DetailView):
	model = IncomingNumber
	template_name = 'phonePlata/incoming_number/detail.html'


class IncomingNumberUpdateView(LoginRequiredMixin, UpdateView):
	model = IncomingNumber
	template_name = 'phonePlat/incoming_number/update.html'
	form_class = CrispyIncomingNumberUpdateForm


class PayingCodeListView(LoginRequiredMixin, ListView):
	model = PayingCode
	template_name = 'phonePlat/paying_code_list.html'
	paginate_by = 30


class AccessLineListView(LoginRequiredMixin, ListView):
	model = AccessLine
	template_name = 'phonePlat/access_line/access_line_list.html'
	paginate_by = 30

	def get_queryset(self):
		query = self.request.GET.get('q', None)
		lookups = (
			Q(location__name__icontains=query) |
			Q(parent_number__number__icontains=query) |
			Q(contract_number__number__icontains=query)
		)
		if query is not None:
			queryset = super().get_queryset().filter(lookups).distinct().order_by('location')
		else:
			queryset = super().get_queryset().order_by('location')
		return queryset


class AccessLineDetailView(LoginRequiredMixin, DetailView):
	model = AccessLine
	template_name = 'phonePlat/access_line/access_line_detail.html'


class AccessLineUpdateView(LoginRequiredMixin, UpdateView):
	model = AccessLine
	template_name = 'phonePlat/access_line/access_line_update.html'
	form_class = CrispyAccessLineUpdateForm
