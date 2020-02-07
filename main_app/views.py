from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Blop, Comment
from .forms import CommentForm

def home(request):
  return render(request, 'main_app/home.html')

def blop_details(request, blop_id):
  blop = Blop.objects.get(id=blop_id)
  return render(request, 'main_app/detail.html', {
    'blop': blop
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('main_app:home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class BlopCreate(CreateView):
  #add something that checks if a user is logged in.
  #if user is not logged in they are redirected to the login page
  model = Blop
  fields = ['title', 'video', 'image', 'article']
  def form_valid(self, form):
    form.instance.creator = self.request.user
    return super().form_valid(form)

def comment_create(request, blop_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.creator = request.user
    new_comment.blop = Blop.objects.get(id=blop_id)
    new_comment.save()
  return redirect('main_app:blop_details', blop_id=blop_id)