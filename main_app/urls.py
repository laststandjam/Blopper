from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('blops/create', views.BlopCreate.as_view(), name='create_blop')
]