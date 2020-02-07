from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Blop(models.Model):
  creator = models.ForeignKey(User, on_delete =models.CASCADE)
  title = models.CharField (max_length=100)
  video  = models.URLField(max_length=200, null=True, blank=True)
  image = models.ImageField(null=True, blank=True)
  article = models.TextField(max_length="1000", blank=True)
  likes = models.PositiveIntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  def get_absolute_url(self):
    return reverse('main_app:home')

class Blopper(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  liked_blops = models.ManyToManyField(Blop)
  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Blopper.objects.create(user=instance)
  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.blopper.save()
    

class Comments(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(max_length= 300)
  created_at = models.DateTimeField(auto_now_add=True)