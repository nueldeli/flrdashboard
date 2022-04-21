from django.urls import path
from .views import figure_index_view, kuching_index_view

urlpatterns = [
	path('', figure_index_view, name='figure_index'),
	path('kuching_index/', kuching_index_view, name='kuching_index'),
]