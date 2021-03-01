from django.contrib import admin
from .models import Poll, PollOptions
# Register your models here.

admin.site.register(Poll)
admin.site.register(PollOptions)
