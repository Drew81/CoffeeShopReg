from __future__ import unicode_literals
from django.db import models


#Items models
class Coffee(models.Model):
	image = models.ImageField(upload_to='item')
	name = models.CharField(max_length=250)
	ingredients = models.TextField(max_length=1000)
	price = models.FloatField()

	def __str__(self):
		return self.name


class Bakery(models.Model):
	image = models.ImageField(upload_to='item')
	name = models.CharField(max_length=250)
	ingredients = models.TextField(max_length=1000)
	price = models.FloatField()

	def __str__(self):
		return self.name


class Food(models.Model):
	image = models.ImageField(upload_to='item')
	name = models.CharField(max_length=250)
	ingredients = models.TextField(max_length=1000)
	price = models.FloatField()

	def __str__(self):
		return self.name

class Register(models.Model):
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField()

	def __str__(self):
		return self.email
