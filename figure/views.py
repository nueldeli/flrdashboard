from django.shortcuts import render
from .models import FigureOverview, PlantingFigure, Division, FigureByDivision
from .forms import UpdateFigureOverviewForm, UpdateFigureByDivisionForm
from django.views.generic import UpdateView
from django.db.models import Sum
#from django.views.generic import TemplateView

# Create your views here.
#class FigureIndexView(TemplateView):
	#template_name = 'figure/figure_index.html'

# Filter based on division name


def figure_index_view(request):
	# Get all class objects
	figure_overview_data = FigureOverview.objects.all()
	figure_by_division_data = FigureByDivision.objects.all()
	planting_figure_data = PlantingFigure.objects.all()

	return render(request, 'figure/figure_index.html', {
		'figure_overview_data':figure_overview_data,
		'figure_by_division_data':figure_by_division_data,
		'planting_figure_data':planting_figure_data 
	})

class UpdateFigureOverviewView(UpdateView):
	model = FigureOverview
	template_name = 'figure/figure_overview_update.html'
	form_class = UpdateFigureOverviewForm

class UpdateFigureByDivisionView(UpdateView):
	model = FigureByDivision
	template_name = 'figure/figure_by_division_update.html'
	form_class = UpdateFigureByDivisionForm