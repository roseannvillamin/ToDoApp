from django.db import models


class TodoItem(models.Model):
	content = models.CharField(max_length=200)
	done = models.BooleanField(default=False)
	
	def __str__(self):
		return self.content