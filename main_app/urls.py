from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'main_app'
urlpatterns = [
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('blops/<int:blop_id>/', views.blop_details, name='blop_details'),
  path('blops/create/', views.blop_create, name='create_blop'),
  path('blops/create/video/', views.blop_create_video, name='create_blop_video'),
  path('blops/create/image/', views.blop_create_image, name='create_blop_image'),
  path('blops/create/article/', views.blop_create_article, name='create_blop_article'),
  path('blops/<int:blop_id>/comment', views.comment_create, name='create_comment'),
  path('blops/<int:blop_id>/comment/<int:comment_id>/delete', views.comment_delete, name='delete_comment'),
  path('blops/<int:blop_id>/comment/<int:comment_id>/edit', views.comment_edit, name='edit_comment'),
  path('blopper/', views.blopper, name='blopper'),
  path('articles/', views.articles, name='articles'),
  path('videos/', views.videos, name='videos'),
  path('images/', views.images, name='images'),
]
