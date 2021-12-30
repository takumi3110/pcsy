# -*- cording:utf-8 -*-

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
