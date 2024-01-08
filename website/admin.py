from django.contrib import admin
from .models import Question, Topic
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question_name']

class TopicAdmin(admin.ModelAdmin):
	list_display = ['topic_name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, TopicAdmin)