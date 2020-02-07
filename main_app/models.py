from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Blopper(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # liked_blops = 
  # my_blops = 
  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Blopper.objects.create(user=instance)
  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.blopper.save()
    
class Blop(models.Model):
  creator = models.ForeignKey(User, on_delete =models.CASCADE)
  title = models.CharField (max_length=100)
  video  = models.URLField(max_length=200)
  image = models.ImageField()
  article = models.TextField(max_length="1000")
  likes = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
  creator = models.ForeignKey(User, on_delete =models.CASCADE)
  content = models.TextField(max_length= 300)
  created_at = models.DateTimeField(auto_now_add=True)
