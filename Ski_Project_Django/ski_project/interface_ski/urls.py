from django.urls import path
from . import views

urlpatterns = [
	path('graph_calculation/', views.graph, name='graph_calculation')
]
