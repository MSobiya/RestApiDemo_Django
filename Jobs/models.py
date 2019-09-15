from django.db import models

#Class based API view is created for this Job Model
class Job(models.Model):
	j_title = models.CharField(max_length=255)
	j_desc = models.TextField()
	j_sal = models.IntegerField()
	j_location = models.CharField(max_length=255)


	def __str__(self):
		return self.j_title