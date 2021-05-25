from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Branches(models.Model):
	name = models.CharField(max_length = 100, primary_key=True)
	discripton = models.TextField(default="Test")
	user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
	count = models.IntegerField(default=0)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('groups')
	def inc(self):
		self.count += 1