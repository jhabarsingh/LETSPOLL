from django import forms
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("first_name","last_name", "username", 
			"email", "password1", "password2", 
		)


class OtpForm(forms.ModelForm):
	class Meta:
		models = Otp 
		fields = ('email', 'otp')


class PollForm(forms.ModelForm):
	class Meta:
		models = Poll
		fields = ["__all__"]


class PollOptionForm(forms.ModelForm):
	class Meta:
		models = PollOptions
		fields = ["__all__"]