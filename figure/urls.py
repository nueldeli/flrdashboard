from django.urls import path
from .views import figure_index_view, UpdateFigureOverviewView, UpdateFigureByDivisionView

urlpatterns = [
	path('', figure_index_view, name='figure_index'),
	path('update_figure_overview/<int:pk>', UpdateFigureOverviewView.as_view(), name='figure_overview_update'),
	path('update_figure_by_division/<int:pk>', UpdateFigureByDivisionView.as_view(), name='figure_by_division_update'),
]