from django import forms

from .models import *


class ServiceForms(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Service
		fields = ('category', 'number', 'name', 'status', 'team', 'holiday', 'remind', 'channel_count', 'start_date',
		          'end_date', 'description')
