from django import forms
from .models import user_details

class user_details_form(forms.ModelForm):
	class Meta:
		model = user_details
		fields={
			'User',
			'password',
		}
