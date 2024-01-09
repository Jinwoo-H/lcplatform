from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Question(models.Model):
	question_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	link = models.CharField(max_length=500)
	notes = models.TextField(blank=True, null=True)
	#topics seperated by a comma
	# topics = models.CharField(max_length=500)
	topics = ArrayField(models.CharField(max_length=200), blank=True)
	difficulty = models.CharField(max_length=20, null=True)
	belongs_to = models.CharField(max_length=100, blank=True)
	favorite = models.BooleanField(default=False)
	code = models.TextField(blank=True, null=True)
	# belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
class Topic(models.Model):
	topic_name = models.CharField(max_length=50)
	belongs_to = models.CharField(max_length=100, blank=True)