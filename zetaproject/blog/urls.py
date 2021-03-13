from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('polls', views.PollIndexView.as_view(), name='pollindex'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name="details"),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('polls/<int:question_id>/vote/', views.vote, name="vote"),
    
    
    path('<int:post_id>/postbody', views.postbody, name="postbody"),
    path('', views.IndexView.as_view(), name='blog'),
]