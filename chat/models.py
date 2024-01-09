from django.db import models

# Create your models here.
class Discussion(models.Model):
	discussion_question = models.CharField(max_length=100)
	discussion_link = models.CharField(max_length=250, blank=True, null=True)
	discussion_details = models.TextField(blank=True, null=True)
	belongs_to = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
