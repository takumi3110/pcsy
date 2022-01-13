from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import *


class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber
	extra = 0


class SurplusNumberInline(admin.TabularInline):
	model = SurplusNumber
	extra = 0


class NotificationInline(admin.TabularInline):
	model = Notification
	extra = 0


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	search_fields = ('name',)
	actions_on_bottom = True


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
	list_display = ('category', 'number', 'status', 'system', 'opening_date', 'updated_date', 'updated_user')
	list_display_links = ('category', 'number', 'status', 'system', 'opening_date', 'updated_date', 'updated_user')
	list_filter = ('category', 'number', 'status', 'system', 'updated_user')
	search_fields = ('category', 'number', 'status', 'system', 'updated_user')
	actions_on_bottom = True
	readonly_fields = ['updated_date']


@admin.register(SurplusNumber)
class SurplusNumberAdmin(admin.ModelAdmin):
	list_display = ('number', 'status', 'system', 'opening_date', 'end_date', 'updated_date', 'updated_user')
	list_display_links = ('number', 'status', 'system', 'opening_date', 'end_date', 'updated_date', 'updated_user')
	list_filter = ('number', 'status', 'system', 'updated_user')
	search_fields = ('number', 'status', 'system', 'updated_user')
	actions_on_bottom = True
	readonly_fields = ['updated_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('category', 'number', 'name', 'status', 'team', 'holiday', 'always', 'remind', 'start_date',
	                'updated_date', 'updated_user')
	list_display_links = ('category', 'number', 'name', 'status', 'team', 'holiday', 'always', 'remind', 'start_date',
	                      'updated_date', 'updated_user')
	list_filter = ('category', 'status', 'holiday', 'always', 'remind', 'team', 'updated_user')
	search_fields = ('number', 'name', 'status', 'team__code', 'updated_user__screenname')
	actions_on_bottom = True
	readonly_fields = ['updated_date']
	formfield_overrides = {
		models.TextField: {
			'widget': Textarea(
				attrs={
					'rows': 2,
					'cols': 40
				}
			)
		}
	}


@admin.register(AccessLine)
class AccessLineAdmin(admin.ModelAdmin):
	list_display = ('parent_number', 'location', 'system', 'status', 'surplus_count', 'allowance_count', 'updated_date',
	                'updated_user')
	list_display_links = ('parent_number', 'location', 'system', 'status', 'surplus_count', 'allowance_count',
	                      'updated_date', 'updated_user')
	list_filter = ('location', 'system', 'status', 'parent_number', 'updated_user')
	search_fields = ('location__name', 'system__name', 'status', 'parent_number__number', 'updated_user__screenname')
	actions_on_bottom = True
	readonly_fields = ['updated_date']
	ordering = ['id']


@admin.register(Trank)
class TrankAdmin(admin.ModelAdmin):
	list_display = ('name', 'location', 'status')
	list_display_links = ('name', 'location', 'status')
	list_filter = ('name', 'location', 'status')
	search_fields = ('name', 'location', 'status')
	actions_on_bottom = True


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
	list_display = ('number', 'name', 'service', 'team', 'status', 'updated_date', 'updated_user')
	list_display_links = ('number', 'name', 'service', 'team', 'status', 'updated_date', 'updated_user')
	list_filter = ('service', 'team', 'status', 'updated_user')
	search_fields = ('service', 'team', 'status', 'updated_user')
	actions_on_bottom = True 
	readonly_fields = ['updated_date']
	formfield_overrides = {
		models.TextField: {
			'widget': Textarea(
				attrs={
					'rows': 3,
					'cols': 80
				}
			)
		}
	}


@admin.register(TrankInfo)
class TrankInfoAdmin(admin.ModelAdmin):
	list_display = ('trank_primary', 'prefix_primary', 'access_line')
	list_display_links = ('trank_primary', 'prefix_primary', 'access_line')
	list_filter = ('trank_primary', 'prefix_primary', 'access_line')
	search_fields = ('trank_primary', 'trank_secondary', 'prefix_primary', 'prefix_primary', 'access_line')
	actions_on_bottom = True 


@admin.register(PayingService)
class PayingServiceAdmin(admin.ModelAdmin):
	list_display = ('abbreviation', 'name', 'career')
	list_display_links = ('abbreviation', 'name', 'career')
	list_filter = ('name', 'career')
	search_fields = ('abbreviation', 'name', 'career')
	actions_on_bottom = True 


@admin.register(IncomingNumber)
class IncomingNumberAdmin(admin.ModelAdmin):
	list_display = ('number', 'paying_service', 'status', 'start_date', 'updated_date', 'updated_user')
	list_display_links = ('number', 'paying_service', 'status', 'start_date', 'updated_date', 'updated_user')
	list_filter = ('number', 'paying_service', 'status', 'updated_user')
	search_fields = ('number', 'paying_service', 'status', 'updated_user')
	actions_on_bottom = True
	readonly_fields = ['updated_date']


@admin.register(PayingCode)
class PayingCodeAdmin(admin.ModelAdmin):
	list_display = ('code', 'status', 'service', 'target', 'dept')
	list_display_links = ('code', 'status', 'service', 'target', 'dept')
	list_filter = ('code', 'status', 'service', 'target', 'dept')
	search_fields = ('code', 'status', 'service', 'target', 'dept')
	actions_on_bottom = True


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('number', 'incoming_number', 'phone_number', 'paying_code')
	list_display_links = ('number', 'incoming_number', 'phone_number', 'paying_code')
	list_filter = ('number', 'incoming_number', 'phone_number', 'paying_code')
	search_fields = ('number', 'incoming_number', 'phone_number', 'paying_code')
	actions_on_bottom = True
