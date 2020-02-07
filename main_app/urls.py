from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'main_app'
urlpatterns = [
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup')
]