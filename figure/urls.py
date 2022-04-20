from django.urls import path
from .views import figure_index_view

urlpatterns = [
	path('', figure_index_view, name='figure_index'),
]