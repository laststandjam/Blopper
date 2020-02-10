from django.forms import ModelForm
from .models import Comment, Blop

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']

class VideoForm(ModelForm):
  class Meta:
    model = Blop
    fields = ['title', 'video']

class ImageForm(ModelForm):
  class Meta:
    model = Blop
    fields = ['title', 'image']

class ArticleForm(ModelForm):
  class Meta:
    model = Blop
    fields = ['title', 'article']