from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Question(models.Model):
	question_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	link = models.CharField(max_length=500)
	notes = models.TextField(blank=True, null=True)
	topics = ArrayField(models.CharField(max_length=200), null=True, blank=True)
	difficulty = models.CharField(max_length=20, null=True, blank=True)
	belongs_to = models.CharField(max_length=100, blank=True)
	favorite = models.BooleanField(default=False)
	code = models.TextField(blank=True, null=True)
	generated_notes = models.TextField(blank=True, null=True)

class Topic(models.Model):
	topic_name = models.CharField(max_length=50)
	belongs_to = models.CharField(max_length=100, blank=True)