from django.contrib import admin

from .models import *
from phonePlat.models import Service, AccessLine, PayingService


class PayingServiceInline(admin.TabularInline):
	model = PayingService
	extra = 0


class ServiceInline(admin.TabularInline):
	model = Service
	extra = 0


class AccessLineInline(admin.TabularInline):
	model = AccessLine
	extra = 0


class CategoryInline(admin.TabularInline):
	model = Category
	extra = 0


class ParentNumberInline(admin.TabularInline):
	model = ParentNumber
	extra = 0


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	search_fields = ('name',)
	inlines = [CategoryInline, PayingServiceInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'career', 'status')
	list_display_links = ('name', 'career', 'status')
	list_filter = ('name', 'career', 'status')
	search_fields = ('name', 'career__name')
	inlines = [ServiceInline, ParentNumberInline]


@admin.register(ContractNumber)
class ContractNumberAdmin(admin.ModelAdmin):
	list_display = ('number', 'location', 'start_date', 'status', 'line_category')
	list_display_links = ('number', 'location', 'start_date', 'status', 'line_category')
	list_filter = ('number', 'location', 'status', 'name', 'place')
	search_fields = ('number', 'location', 'name', 'place')
	actions_on_bottom = True
	inlines = [ServiceInline, AccessLineInline]


@admin.register(ParentNumber)
class ParentNumberAdmin(admin.ModelAdmin):
	list_display = ('number', 'status', 'line_category')
	list_display_links = ('number', 'status', 'line_category')
	list_filter = ('number', 'status', 'line_category')
	search_fields = ('number', 'line_category__name')
	ordering = ['number']
	actions_on_bottom = True
	inlines = [ServiceInline, AccessLineInline]
