from django import form
from .models import *


class PollForm(forms.ModelForm):
	class Meta:
		models = Poll
		fields = ["__all__"]

class PollOptionForm(forms.ModelForm):
	class Meta:
		models = PollOption
		fields = ["__all__"]