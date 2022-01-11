from django_filters import rest_framework as filters

from .models import *


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
