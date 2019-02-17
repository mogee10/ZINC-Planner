from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event (models.Model):
	organizer = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	image = models.ImageField()
	name = models.CharField(max_length=120)
	description = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.name
