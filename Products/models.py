from django.db import models

#Function based API view is created for this in views.py file
class Product(models.Model):
	title = models.CharField(max_length = 100)
	url = models.TextField()
	publish_date = models.DateTimeField()
	#image = models.ImageField(upload_to = 'images/')
	#icon = models.ImageField(upload_to = 'images/')
	description = models.TextField()
	#votes = models.IntegerField(default=0)
	price = models.IntegerField()


	def __str__(self):
		return self.title
