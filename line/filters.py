from django_filters import rest_framework as filters

from .models import *


class CareerFilter(filters.FilterSet):
	class Meta:
		model = Career
		fields = ['name']


class CategoryFilter(filters.FilterSet):
	class Meta:
		model = Category
		fields = ['name', 'career']


class ContractNumberFilter(filters.FilterSet):
	class Meta:
		model = ContractNumber
		fields = ['number', 'location', 'name', 'line_category']


class ParentNumberFilter(filters.FilterSet):
	class Meta:
		model = ParentNumber
		fields = ['number', 'line_category']
