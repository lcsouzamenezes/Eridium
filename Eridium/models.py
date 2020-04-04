from django.db import models
from datetime import datetime

# Create your models here.
# I have used three fields/columns/attributes of the class

""" file_name: To save the name of file to be uploaded by the user.
	file_url: To save the url of the location where the file is to be saved.
	last_update: to store date and time. Automatically set the field to now every time the object is saved using auto_now = True
"""

class file_storage(models.Model):
	file_name = models.CharField(max_length=255)
	file_url = models.TextField()
	last_update = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.file_name

