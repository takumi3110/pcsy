from rest_framework import serializers

from .models import *


class SiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Site
		fields = ('id', 'name', 'status', 'description', 'version', 'updated_date', 'updated_user')


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


class CareerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Career
		fields = ('id', 'name',)


class LineCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = LineCategory
		fields = ('id', 'name', 'status', 'career')


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('id', 'name', 'address', 'description')


class ContractNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContractNumber
		fields = ('id', 'number', 'location', 'status', 'start_date', 'name', 'place', 'line_category',
		          'description', 'version')


class ParentNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = ParentNumber
		fields = ('id', 'number', 'career', 'status', 'line_category', 'description')


class SystemSerializer(serializers.ModelSerializer):
	class Meta:
		model = System
		fields = ('id', 'name',)


class PhoneNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = PhoneNumber
		fields = ('id', 'category', 'number', 'status', 'system', 'opening_date', 'end_date', 'start_date',
		          'obsolete_date', 'interrupt_date', 'paying', 'ticket', 'description', 'updated_date',
		          'updated_user')


class SurplusNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = SurplusNumber
		fields = ('id', 'number', 'status', 'system', 'opening_date', 'end_date', 'ticket', 'description',
		          'updated_date, updated_user')


class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ('id', 'number', 'name', 'status', 'team', 'holiday', 'always', 'start_date', 'end_date', 'remind',
		          'channel_count', 'description', 'mail_address', 'file', 'version', 'updated_date', 'updated_user',
		          'contract_number', 'line_category', 'parent_number')
 
 
class AccessLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccessLine
		fields = ('id', 'location', 'system', 'status', 'career', 'line_category', 'parent_number', 'opening_date',
		          'contract_number', 'proportion', 'surplus_count', 'allows_count', 'threshold_value', 'updated_date',
		          'updated_user')


class TrankSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trank
		fields = ('id', 'name', 'location', 'status', 'description')


class ScenarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Scenario
		fields = ('id', 'number', 'name', 'service', 'team', 'description', 'status', 'updated_user', 'updated_date')


class TrankInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrankInfo
		fields = ('id', 'trank_primary', 'trank_secondary', 'prefix_primary', 'prefix_secondary', 'access_line')


class PayingServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = PayingService
		fields = ('id', 'name', 'career')


class IncomingNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = IncomingNumber
		fields = ('id', 'number', 'paying_service', 'status', 'holder', 'channel_count', 'start_date', 'country',
		          'description', 'updated_user', 'updated_date')


class PayingCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = PayingCode
		fields = ('id', 'code', 'status', 'service', 'dept', 'target', 'start_date', 'end_date', 'tems', 'tems_date',
		          'file', 'ticket_number')


class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('id', 'number', 'incoming_number', 'phone_number', 'description', 'paying_code')
