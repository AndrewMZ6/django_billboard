from django.db import models

# Create your models here.
class MyTestModel(models.Model):
	name = models.CharField(max_length=300)
	age = models.IntegerField()

