from django.db import models

# Create your models here.
class Blop(models.Model):
    Title = models.CharField (max_length=100)
    
    