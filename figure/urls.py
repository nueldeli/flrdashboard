from django.urls import path
from .views import FigureIndexView

urlpatterns = [
	path('', FigureIndexView.as_view(), name='figure_index'),
]