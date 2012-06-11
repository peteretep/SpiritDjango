from django.db import models

class Home (models.Model):
    textblock = models.TextField()
class Tours (models.Model):
    tours = models.TextField()
class Angling (models.Model):
    angling = models.TextField()
class Wildlife (models.Model):
    wildlife = models.TextField()
    
# Create your models here.
