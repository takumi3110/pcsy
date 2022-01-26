from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Row, Column, Submit

from .models import *


def css_class(column, bottom):
	col = 'col-' + str(column)
	margin_bottom = 'mb-' + str(bottom)
	return 'form-group ' + col + ' ' + margin_bottom

class ServiceUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
		self.fields['holiday'].widget.attrs['class'] = 'form-check-input'

	class Meta:
		model = Service
		fields = ('category', 'number', 'name', 'status', 'team', 'holiday', 'remind', 'channel_count', 'start_date',
		          'end_date', 'description')


class CrispyServiceUpdateForm(ServiceUpdateForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('number', css_class='form-group col-6 mb-3')
			),
			Row(
				Column('name', css_class='form-group col-12 mb-3')
			),
			Row(
				Column('status', css_class='form-group col-6 mb-3'),
				Column('team', css_class='form-group col-6 mb-3')
			),
			Row(
				Column('start_date', css_class='form-group col-6 mb-3'),
				Column('end_date', css_class='form-group col-6 mb-3')
			),
			Row(
				Column('remind', css_class='form-group col-6 mb-3'),
				Column('channel_count', css_class='form-group col-6 mb-3')
			),
			'holiday',
			Row(
				Column('description', css_class='form-group col-12 mb-3')
			),
			Submit('submit', '更新', css_class='col-12 btn btn-block btn-info')
		)


class ScenarioUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Scenario
		fields = ('number', 'name', 'service', 'team', 'status', 'description')


class CrispyScenarioUpdateForm(ScenarioUpdateForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('number', css_class='form-group col-6 mb-3')
			),
			Row(
				Column('name', css_class='form-group col-12 mb-3')
			),
			Row(
				Column('status', css_class='form-group col-6 mb-3'),
				Column('team', css_class='form-group col-6 mb-3')
			),
			Row(
				Column('description', css_class='form-group col-12 mb-3')
			),
			Submit('submit', '更新', css_class='col-12 btn btn-block btn-info')
		)


class PhoneNumberUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = PhoneNumber
		fields = ('number', 'status', 'system', 'parent_number', 'dept', 'opening_date', 'end_date', 'start_date',
		          'obsolete_date', 'interrupt_date', 'paying', 'service', 'ticket', 'description')


class CrispyPhoneNumberUpdateForm(PhoneNumberUpdateForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('category', css_class=css_class(6, 3)),
			),
			Row(
				Column('number', css_class=css_class(6, 3)),
			),
			Row(
				Column('status', css_class=css_class(6, 3)),
				Column('system', css_class=css_class(6, 3))
			),
			Row(
				Column('parent_number', css_class=css_class(6, 3)),
				Column('dept', css_class=css_class(6, 3))
			),
			Row(
				Column('opening_date', css_class=css_class(6, 3)),
				Column('end_date', css_class=css_class(6, 3))
			),
			Row(
				Column('start_date', css_class=css_class(6, 3)),
				Column('obsolete_date', css_class=css_class(6, 3))
			),
			Row(
				Column('interrupt_date', css_class=css_class(6, 3)),
				Column('paying', css_class=css_class(6,3))
			),
			Row(
				Column('service', css_class=css_class(12, 3))
			),
			Row(
				Column('ticket', css_class=css_class(6, 3))
			),
			Row(
				Column('description', css_class=css_class(12, 3))
			),
			Submit('submit', '更新', css_class='col-12 btn btn-block btn-info')
		)


class AccessLineUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = AccessLine
		fields = ('location', 'system', 'status', 'parent_number', 'opening_date', 'contract_number', 'proportion',
		          'surplus_count', 'allowance_count', 'threshold_value')


class CrispyAccessLineUpdateForm(AccessLineUpdateForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout()
