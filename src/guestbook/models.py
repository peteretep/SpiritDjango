from django.db import models
from django.forms import ModelForm


class Review (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    entry = models.TextField()
    checked = models.BooleanField()
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = 'checked'
    

