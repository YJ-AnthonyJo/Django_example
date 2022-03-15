from django.urls import path
from . import views

app_name = 'polls' # using in index.html third a tag

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #generic.DetailView expect captured from url key name is 'pk'
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#above : using generic views
#below : not using generic views
# urlpatterns = [
#     path('', views_.index, name='index'),
#     path('<int:question_id>/', views_.detail, name = 'detail'),
#     path('<int:question_id>/result/', views_.results, name = 'results'),
#     path('<int:question_id>/vote/', views_.vote, name = 'vote'),
# ]