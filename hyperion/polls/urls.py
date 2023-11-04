from django.urls import path, include 
from . import views

#so we can in use the url tag {% url 'polls:detail/results' question_id %}
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="poll"),
    path('<int:question_id>',views.detail, name= 'detail'),
    path('<int:question_id>/results/',views.results, name ='results'),
    path('<int:question_id>/vote/',views.votes, name='vote')
    ]