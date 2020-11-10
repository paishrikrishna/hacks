from django.db import models

# Create your models here.
class user_details(models.Model):
	User = models.TextField(default='n/a')
	password = models.TextField(default='N/A')
	