from django.db import models

class Product(models.Model):
	title		=models.TextField()
	description	=models.TextField()
	price		=models.TextField()
	

class ABC_123(models.Model):
	title		=models.TextField()
	description	=models.TextField()
	price		=models.TextField()
	Flag        =models.TextField()
	
class ABC(models.Model):
	title		=models.TextField()
	description	=models.TextField()
	price		=models.TextField()
	Flag		=models.TextField()


