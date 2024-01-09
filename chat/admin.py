from django.contrib import admin
from .models import Discussion


class DiscussionAdmin(admin.ModelAdmin):
	list_display = ['discussion_question']
# Register your models here.
admin.site.register(Discussion, DiscussionAdmin)