from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'main_app'
urlpatterns = [
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('blops/<int:blop_id>/', views.blop_details, name='blop_details'),
  path('blops/create', views.BlopCreate.as_view(), name='create_blop'),
  path('blops/<int:blop_id>/comment', views.comment_create, name='create_comment'),
  path('blopper/', views.blopper, name='blopper'),
  path('articles/', views.articles, name='articles'),
  path('videos/', views.videos, name='videos'),
  path('images/', views.images, name='images'),
]