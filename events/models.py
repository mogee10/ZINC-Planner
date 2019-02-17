from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event (models.Model):
	image = models.ImageField()
	name = models.CharField(max_length=120)
	description = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.name
