from pdf import views
from django.urls import path

urlpatterns = [
	path('', views.create, name = 'profile'),
	path('<int:pk>/', views.resume, name='resume'),
	path('list', views.profile, name ='list'),
]