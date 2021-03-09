from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	# path('', views.index, name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# the 'name' value as called by the {% url %} template(/idex.html) tag
	# giving arbitrary url path('anything/<int:question_id>/', views.detail, name='detail')	
	# "<int:question_id>/"" gives url path with int, ex polls/5 gives question 5
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]