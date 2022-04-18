from django.urls import path
from .views import figure_index_view, UpdateFigureOverviewView, UpdateFigureByDivisionView, PlantingFigureIndexView, PlantingFigureDetailView, AddPlantingFigureView, UpdatePlantingFigureView, DeletePlantingFigureView

urlpatterns = [
	path('', figure_index_view, name='figure_index'),
	path('update_figure_overview/<int:pk>', UpdateFigureOverviewView.as_view(), name='figure_overview_update'),
	path('update_figure_by_division/<int:pk>', UpdateFigureByDivisionView.as_view(), name='figure_by_division_update'),\
	path('planting_figure_index/', PlantingFigureIndexView.as_view(), name='planting_figure_index'),
	path('planting_figure_detail/<int:pk>', PlantingFigureDetailView.as_view(), name='planting_figure_detail'),
	path('add_planting_figure/', AddPlantingFigureView.as_view(), name='planting_figure_add'),
	path('update_planting_figure/<int:pk>', UpdatePlantingFigureView.as_view(), name='planting_figure_update'),
	path('delete_planting_figure/<int:pk>', DeletePlantingFigureView.as_view(), name='planting_figure_delete')
]