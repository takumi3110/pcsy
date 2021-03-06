# -*- cording:utf-8 -*-

from rest_framework import serializers

from .models import *


class SiteSerializer(serializer.ModelSerializer):
	class Meta:
		model = Site
		fields = ('name', 'status', 'description', 'version', 'updated_date', 'updated_user')


class TenantSerializer(serializer.ModelSerializer):
	class Meta:
		model = Tenant
		fields = ('name', 'site', 'description')


class TeamSerializer(serializer.ModelSerializer):
	class Meta:
		model = Team
		fields = ('name', 'code', 'description', 'tenant', 'bcp_tenant', 'start_date', 'end_date',
		          'status', 'proportion', 'contact_user')


class DeptSerializer(serializer.ModelSerializer):
	class Meta:
		model = Dept
		fields = ('name', 'code', 'status', 'aggregate_date', 'active', 'team')


class CareerSerializer(serializer.ModelSerializer):
	class Meta:
		model = Career
		fields = ('name',)


class LineCategorySerializer(serializer.ModelSerializer):
	class Meta:
		model = LineCategory
		fields = ('name', 'status', 'career')


class LocationSerializer(serializer.ModelSerializer):
	class Meta:
		model = Location
		fields = ('name', 'address', 'description')


class ContractNumberSerializer(serializer.ModelSerializer):
	class Meta:
		model = ContractNumber
		fields = ('number', 'location', 'status', 'start_date', 'name', 'place', 'line_category',
		          'description', 'version')


class ParentNumberSerializer(serializer.ModelSerializer):
	class Meta:
		model = ParentNumber
		fields = ('number', 'career', 'status', 'line_category', 'description')


class SystemSerializer(serializer.ModelSerializer):
	class Meta:
		model = System
		fields = ('name',)


class PhoneNumberSerializer(serializer.ModelSerializer):
	class Meta:
		model = PhoneNumber
		fields = ('category', 'number', 'status', 'system', 'opening_date', 'end_date', 'start_date',
		          'obsolete_date', 'interrupt_date', 'paying', 'ticket', 'description', 'updated_date',
		          'updated_user')


class SurplusNumberSerializer(serializer.ModelSerializer):
	class Meta:
		model = SurplusNumber
		fields = ('number', 'status', 'system', 'opening_date', 'end_date', 'ticket', 'description',
		          'updated_date, updated_user')


class ServiceSerializer(serializer.ModelSerializer):
	class Meta:
		model = Service
		fields = ('number', 'name', 'status', 'team', 'holiday', 'always', 'start_date', 'end_date', 'remind',
		          'channel_count', 'description', 'mail_address', 'file', 'version', 'updated_date', 'updated_user',
		          'contract_number', 'line_category', 'parent_number')
 
 
class AccessLineSerializer(serializer.ModelSerializer):
	class Meta:
		model = AccessLine
		fields = ('location', 'system', 'status', 'career', 'line_category', 'parent_number', 'opening_date',
		          'contract_number', 'proportion', 'surplus_count', 'allows_count', 'threshold_value', 'updated_date',
		          'updated_user')


class TrankSerializer(serializer.ModelSerializer):
	class Meta:
		model = Trank
		fields = ('name', 'location', 'status', 'description')


class ScenarioSerializer(serializer.ModelSerializer):
	class Meta:
		model = Scenario
		fields = ('number', 'name', 'service', 'team', 'description', 'status', 'updated_user', 'updated_date')


class TrankInfoSerializer(serializer.ModelSerializer):
	class Meta:
		model = TrankInfo
		fields = ('trank_primary', 'trank_secondary', 'prefix_primary', 'prefix_secondary', 'access_line')


class PayingServiceSerializer(serializer.ModelSerializer):
	class Meta:
		model = PayingService
		fields = ('name', 'career')


class IncomingNumberSerializer(serializer.ModelSerializer):
	class Meta:
		model = IncomingNumber
		fields = ('number', 'paying_service', 'status', 'holder', 'channel_count', 'start_date', 'country',
		          'description', 'updated_user', 'updated_date')


class PayingCodeSerializer(serializer.ModelSerializer):
	class Meta:
		model = PayingCode
		fields = ('code', 'status', 'service', 'dept', 'target', 'start_date', 'end_date', 'tems', 'tems_date',
		          'file', 'ticket_number')


class NotificationSerializer(serializer.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('number', 'incoming_number', 'phone_number', 'description', 'paying_code')
