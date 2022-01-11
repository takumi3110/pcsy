from rest_framework import serializers

from .models import *


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
		fields = ('id', 'category', 'number', 'name', 'status', 'team', 'holiday', 'always', 'start_date', 'end_date',
		          'remind', 'channel_count', 'description', 'mail_address', 'file', 'version', 'updated_date',
		          'updated_user', 'contract_number', 'line_category', 'parent_number')
 
 
class AccessLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccessLine
		fields = ('id', 'location', 'system', 'status', 'parent_number', 'opening_date', 'contract_number', 'proportion',
		          'surplus_count', 'allowance_count', 'threshold_value', 'updated_date', 'updated_user')


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
