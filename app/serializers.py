from .models import Poll, PollOptions
from rest_framework import serializers
from django.contrib.auth.models import User 

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOptions
        fields = ['id', 'option', 'value']

class PollSerializer(serializers.ModelSerializer):
    poll_option = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'question', 'poll_option']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["first_name","last_name", "username", 
			"email", "password1", "password2", 
		]