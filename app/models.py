from django.db import models
import uuid
# Create your models here.

class Poll(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	question = models.CharField(max_length=100)

	def __str__(self):
		return self.question

class PollOptions(models.Model):
	question = models.ForeignKey(Poll, related_name='poll_option', on_delete=models.CASCADE)
	option = models.CharField(max_length=100)
	value = models.IntegerField(default=0)

	def __str__(self):
		return self.question.question