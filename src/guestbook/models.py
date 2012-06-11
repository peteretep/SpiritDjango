from django.db import models

class Review (models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    entry = models.CharField(max_length=500)
    

# Create your models here.
