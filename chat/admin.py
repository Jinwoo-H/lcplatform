from django.contrib import admin
from .models import Discussion, Chat


class DiscussionAdmin(admin.ModelAdmin):
	list_display = ['discussion_question']

class ChatAdmin(admin.ModelAdmin):
	list_display = ['content', 'room']
# Register your models here.
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Chat, ChatAdmin)