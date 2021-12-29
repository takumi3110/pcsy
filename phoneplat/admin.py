from django.contrib import admin

from .models import *


class TenantInline(admin.TabularInline):
	model = Tenant
	extra = 0


class TeamInline(admin.TabularInline):
	model = Team
	extra = 0


class LineCategoryInline(admin.TabularInline):
	model = LineCategory
	extra = 0


class ParentNumberInline(admin.TabularInline):
	model = ParentNumber
	extra = 0


class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber
	extra = 0


class SurplusNumberInline(admin.TabularInline):
	model = SurplusNumber
	extra = 0


class ServiceInline(admin.TabularInline):
	model = Service
	extra = 0


class AccessLineInline(admin.TabularInline):
	model = AccessLine
	extra = 0


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')
	list_display_links = ('name',)
	list_filter = ('name', 'status')
	search_fields = ('name',)
	inlines = [TenantInline]


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
	list_display = ('name', 'site')
	list_display_links = ('name', 'site')
	list_filter = ('name', 'site')
	search_fields = ('name', 'site')
	inlines = [TeamInline]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'tenant', 'status')
	list_display_links = ('name', 'code', 'tenant')
	list_filter = ('name', 'code')
	search_fields = ('name', 'code')
	actions_on_bottom = True
	inlines = [ServiceInline, ]


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'team', 'status', 'active')
	list_display_links = ('name', 'code', 'team')
	list_filter = ('name', 'code', 'status', 'team')
	search_fields = ('name', 'code', 'team')
	actions_on_bottom = True


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	search_fields = ('name',)
	inlines = [LineCategoryInline]


@admin.register(LineCategory)
class LineCategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'career', 'status')
	list_display_links = ('name', 'career', 'status')
	list_filter = ('name', 'career', 'status')
	search_fields = ('name', 'career', 'status')
	inlines = [ServiceInline, AccessLineInline]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	list_display_links = ('name', 'address')
	list_filter = ('name',)
	search_fields = ('name',)


@admin.register(ContractNumber)
class ContractNumberAdmin(admin.ModelAdmin):
	list_display = ('number', 'location', 'start_date', 'status', 'line_category')
	list_display_links = ('number', 'location', 'start_date', 'status', 'line_category')
	list_filter = ('number', 'location', 'status', 'name', 'place')
	search_fields = ('number', 'location', 'name', 'place')
	actions_on_bottom = True
	inlines = [ServiceInline, AccessLineInline]


@admin.register(ParentNumber)
class ParentNumberAdmin(admin.modelAdmin):
	list_display = ('number', 'career', 'status', 'line_category')
	list_display_links = ('number', 'career', 'status', 'line_category')
	list_filter = ('number', 'career', 'status', 'line_category')
	search_fields = ('number', 'career', 'line_category')
	actions_on_bottom = True
	inlines = [ServiceInline, AccessLineInline]


@admin.register(System)
class SystemAdmin(admin.modelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	search_fields = ('name',)
	actions_on_bottom = True


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.modelAdmin):
	list_display = ('category', 'number', 'status', 'system', 'opening_date', 'updated_date', 'updated_user')
	list_display_links = ('category', 'number', 'status', 'system', 'opening_date', 'updated_date', 'updated_user')
	list_filter = ('category', 'number', 'status', 'system', 'updated_user')
	search_fields = ('category', 'number', 'status', 'system', 'updated_user')
	actions_on_bottom = True


@admin.register(SurplusNumber)
class SurplusNumberAdmin(admin.modelAdmin):
	list_display = ('number', 'status', 'system', 'opening_date', 'end_date', 'updated_date', 'updated_user')
	list_display_links = ('number', 'status', 'system', 'opening_date', 'end_date', 'updated_date', 'updated_user')
	list_filter = ('number', 'status', 'system', 'updated_user')
	search_fields = ('number', 'status', 'system', 'updated_user')
	actions_on_bottom = True


@admin.register(Service)
class ServiceAdmin(admin.modelAdmin):
	list_display = ('number', 'name', 'status', 'team', 'holiday', 'always', 'remind', 'start_date', 'updated_date',
	                'updated_user')
	list_display_links = ('number', 'name', 'status', 'team', 'holiday', 'always', 'remind', 'start_date',
	                      'updated_date', 'updated_user')
	list_filter = ('number', 'name', 'status', 'team', 'holiday', 'always', 'remind', 'updated_user')
	search_fields = ('number', 'name', 'status', 'team', 'updated_user')
	actions_on_bottom = True


@admin.register(AccessLine)
class AccessLineAdmin(admin.modelAdmin):
	list_display = ('location', 'system', 'status', 'career', 'line_category', 'parent_number', 'opening_date',
	                'updated_date', 'updated_user')
	list_display_links = ('location', 'system', 'status', 'career', 'line_category', 'parent_number',
	                      'opening_date', 'updated_date', 'updated_user')
	list_filter = ('location', 'system', 'status', 'career', 'line_category', 'parent_number', 'updated_user')
	search_fields = ('location', 'system', 'status', 'career', 'line_category', 'parent_number', 'updated_user')
	actions_on_bottom = True


@admin.register(Trank)
class TrankAdmin(admin.modelAdmin):
	list_display = ('name', 'location', 'status')
	list_display_links = ('name', 'location', 'status')
	list_filter = ('name', 'location', 'status')
	search_fields = ('name', 'location', 'status')
	actions_on_bottom = True


@admin.register(Scenario)
class ScenarioAdmin(admin.modelAdmin):
	list_display = ('number', 'name', 'service', 'team', 'status', 'updated_date', 'updated_user')
	list_display_links = ('number', 'name', 'service', 'team', 'status', 'updated_date', 'updated_user')
	list_filter = ('service', 'team', 'status', 'updated_user')
	search_fields = ('service', 'team', 'status', 'updated_user')
	actions_on_bottom = True 


@admin.register(TrankInfo)
class TrankInfoAdmin(admin.modelAdmin):
	list_display = ('trank_primary', 'prefix_primary', 'access_line')
	list_display_links = ('trank_primary', 'prefix_primary', 'access_line')
	list_filter = ('trank_primary', 'prefix_primary', 'access_line')
	search_fields = ('trank_primary', 'trank_secondary', 'prefix_primary', 'prefix_primary', 'access_line')
	actions_on_bottom = True 


@admin.register(PayingService)
class PayingServiceAdmin(admin.modelAdmin):
	list_display = ('name', 'career')
	list_display_links = ('name', 'career')
	list_filter = ('name', 'career')
	search_fields = ('name', 'career')
	actions_on_bottom = True 


@admin.register(IncomingNumber)
class IncomingNumberAdmin(admin.modelAdmin):
	list_display = ('number', 'paying_service', 'status', 'start_date', 'updated_date', 'updated_user')
	list_display_links = ('number', 'paying_service', 'status', 'start_date', 'updated_date', 'updated_user')
	list_filter = ('number', 'paying_service', 'status', 'updated_user')
	search_fields = ('number', 'paying_service', 'status', 'updated_user')
	actions_on_bottom = True


@admin.register(PayingCode)
class PayingCodeAdmin(admin.modelAdmin):
	list_display = ('code', 'status', 'service', 'target', 'dept', 'updated_date', 'updated_user')
	list_display_links = ('code', 'status', 'service', 'target', 'dept', 'updated_date', 'updated_user')
	list_filter = ('code', 'status', 'service', 'target', 'dept', 'updated_user')
	search_fields = ('code', 'status', 'service', 'target', 'dept', 'updated_user')
	actions_on_bottom = True


@admin.register(Notification)
class NotificationAdmin(admin.modelAdmin):
	list_display = ('number', 'incoming_number', 'phone_number', 'paying_code')
	list_display_links = ('number', 'incoming_number', 'phone_number', 'paying_code')
	list_filter = ('number', 'incoming_number', 'phone_number', 'paying_code')
	search_fields = ('number', 'incoming_number', 'phone_number', 'paying_code')
	actions_on_bottom = True
