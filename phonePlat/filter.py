from django_filters import rest_framework as filters

from .models import *


class ServiceFilter(filters.FilterSet):
	class Meta:
		model = Service
		fields = ['id', 'category', 'number', 'team']
