from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Row, Column, Submit

from .models import *


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
