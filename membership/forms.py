from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	class Meta:
			model = User
			fields = ('first_name', 'last_name', 'username', 'email', 'password')

			widgets = {
				'first_name':forms.TextInput(),
				'last_name':forms.TextInput(),
				'username':forms.TextInput(),
				'email':forms.EmailInput(),
				'password':forms.PasswordInput()
			}

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user