from django_filters import rest_framework as filters

from .models import *


class SystemFilter(filters.FilterSet):
	class Meta:
		model = System
		fields = ['id', 'name']


class ServiceFilter(filters.FilterSet):
	class Meta:
		model = Service
		fields = ['id', 'category', 'number', 'team']


class ScenarioFilter(filters.FilterSet):
	class Meta:
		model = Scenario
		fields = ['id', 'number', 'name', 'service', 'team']


class AccessLineFilter(filters.FilterSet):
	class Meta:
		model = AccessLine
		fields = ['id', 'location', 'system', 'status', 'parent_number', 'contract_number', 'updated_user']


class PhoneNumberFilter(filters.FilterSet):
	class Meta:
		model = PhoneNumber
		fields = ['id', 'category', 'number', 'system', 'paying', 'scenario', 'ticket']


class SurplusNumberFilter(filters.FilterSet):
	class Meta:
		model = SurplusNumber
		fields = ['id', 'number', 'system', 'ticket']


class TrankFilter(filters.FilterSet):
	class Meta:
		model = Trank
		fields = ['id', 'name', 'location']


class TrankInfoFilter(filters.FilterSet):
	class Meta:
		model = Trank
		fields = ['id', 'trank_primary', 'trank_secondary', 'prefix_primary', 'prefix_secondary', 'access_line']


class PayingServiceFilter(filters.FilterSet):
	class Meta:
		model = PayingService
		fields = ['id', 'name', 'abbreviation', 'career']


class IncomingNumberFilter(filters.FilterSet):
	class Meta:
		model = IncomingNumber
		fields = ['id', 'number', 'paying_service', 'holder', 'service']


class PayingCodeFilter(filters.FilterSet):
	class Meta:
		model = PayingCode
		fields = ['id', 'code', 'service', 'dept', 'target']


class NotificationFilter(filters.FilterSet):
	class Meta:
		model = Notification
		fields = ['id', 'number', 'incoming_number', 'phone_number', 'paying_code']
