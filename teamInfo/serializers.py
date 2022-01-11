from rest_framework import serializers

from .models import *


class SiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Site
		fields = ('id', 'name', 'category', 'status', 'description', 'version', 'updated_date', 'updated_user')


class TenantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tenant
		fields = ('id', 'name', 'site', 'description')


class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ('id', 'name', 'code', 'description', 'tenant', 'bcp_tenant', 'start_date', 'end_date',
		          'status', 'proportion', 'updated_date', 'updated_user')


class DeptSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dept
		fields = ('id', 'code', 'name', 'status', 'aggregate_code', 'active', 'team')


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('id', 'name', 'address', 'description')
