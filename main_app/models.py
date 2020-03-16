from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from embed_video.fields import EmbedVideoField

class Blop(models.Model):
  creator = models.ForeignKey(User, on_delete =models.CASCADE)
  title = models.CharField (max_length=50)
  video  = EmbedVideoField(max_length=200, null=True, blank=True) 
  image = models.URLField(max_length=200, null=True, blank=True)
  article = models.TextField(max_length=10000, blank=True)
  likes = models.PositiveIntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  def get_absolute_url(self):
    return reverse('main_app:home')
  def __str__(self):
    if len(self.article) < 150:
      return self.article[:150]
    return self.article[:150] + "..."
  class Meta():
    ordering = ['-likes']

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

class Comment(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(max_length= 300)
  blop = models.ForeignKey(Blop, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta():
    ordering = ['-created_at']
  def __str__(self):
    return f'{self.content}'