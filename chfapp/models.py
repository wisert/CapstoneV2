from django.db import models

# Create your models here. 
# Structuring forms, mapping fields, storing in database table.

class CreateAccount(models.Model):
	#inherits from Model class
	first_name = models.CharField(max_length=10, default='',blank=False)
	last_name = models.CharField(max_length=10,default='',blank=False)
	username = models.CharField(max_length=10,default='',blank=False)
	password = models.CharField(max_length=10,default='',blank=False)
	email = models.EmailField()
	organization = models.CharField(max_length=50,default='',blank=False, null=True)
	#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) for things that are only added once
	#updated = models.DateTimeField(auto_now_add=False, auto_now=True) for updating timestamps frequently

	def __str__(self): #python3 uses __str__
		return self.email