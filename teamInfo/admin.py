from django.contrib import admin

from .models import *
from phoneplat.models import Service


class ServiceInline(admin.TabularInline):
	model = Service
	extra = 0


class TenantInline(admin.TabularInline):
	model = Tenant
	extra = 0


class TeamInline(admin.TabularInline):
	model = Team
	extra = 0
	fk_name = 'tenant'


class DeptInline(admin.TabularInline):
	model = Dept
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
	list_display = ('name', 'code', 'tenant', 'status', 'updated_date')
	list_display_links = ('name', 'code', 'tenant', 'updated_date')
	list_filter = ('name', 'code')
	search_fields = ('name', 'code')
	actions_on_bottom = True
	inlines = [ServiceInline, DeptInline]
	readonly_fields = ['updated_date']


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'team', 'status', 'active')
	list_display_links = ('name', 'code', 'team')
	list_filter = ('name', 'code', 'status', 'team')
	search_fields = ('name', 'code', 'team')
	actions_on_bottom = True


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	list_display_links = ('name', 'address')
	list_filter = ('name',)
	search_fields = ('name',)
