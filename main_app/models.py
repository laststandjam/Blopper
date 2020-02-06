from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blop(models.Model):
    creator = models.ForeignKey(User, on_delete =models.CASCADE)
    title = models.CharField (max_length=100)
    content  = models.URLField(max_length=200)
    article = models.TextField(max_length="1000")
    likes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    creator = models.ForeignKey(User, on_delete =models.CASCADE)
    content = models.TextField(max_length= 300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    