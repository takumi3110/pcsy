from django_filters import rest_framework as filters

from .models import *


class TenantFilter(filters.FilterSet):
	class Meta:
		model = Tenant
		fields = ['id', 'name']


class TeamFilter(filters.FilterSet):
	class Meta:
		model = Team
		fields = ['id', 'name', 'code']


class DeptFilter(filters.FilterSet):
	class Meta:
		model = Dept
		fields = ['name', 'code']
