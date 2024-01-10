from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Discussion(models.Model):
	discussion_question = models.CharField(max_length=100)
	discussion_link = models.CharField(max_length=250, blank=True, null=True)
	discussion_details = models.TextField(blank=True, null=True)
	belongs_to = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
	content = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.CharField(max_length=1000)

