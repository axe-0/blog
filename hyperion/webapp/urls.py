
from django.urls import path, include 
from . import views
app_name = 'webhome'
urlpatterns = [
    path('', views.index, name="home"),
    ]