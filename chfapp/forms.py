from django import forms

from .models import CreateAccount

#Form appears when you choose to add user in the .../admin/createaccount page
class CreateAccountForm(forms.ModelForm):
	class Meta:
		model = CreateAccount
		fields = ['email','organization']
	#self = instance of form
	def clean_email(self):
		email = self.cleaned_data.get('email')
		# email_base, provider = email.split("@")
		# domain, extension = provider.split('.')
		# if not extension == "edu":
		# 	raise forms.ValidationError("Please use an academic email address.")
		return email

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		return first_name


