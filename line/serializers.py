from rest_framework import serializers

from .models import *


class CareerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Career
		fields = ('id', 'name',)


class LineCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = LineCategory
		fields = ('id', 'name', 'status', 'career')


class ContractNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContractNumber
		fields = ('id', 'number', 'location', 'status', 'start_date', 'name', 'place', 'line_category',
		          'description', 'version')


class ParentNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = ParentNumber
		fields = ('id', 'number', 'career', 'status', 'line_category', 'description')
