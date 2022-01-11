from django_filters import rest_framework as filters

from .models import *


class SiteFilter(filters.FilterSet):
	class Meta:
		model = Site
		fields = ['name', 'category']


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
		fields = ['id', 'name', 'code']


class LocationFilter(filters.FilterSet):
	class Meta:
		model = Location
		fields = ['name']
