from django.shortcuts import render
from .models import FigureOverview, PlantingFigure, Division
from django.db.models import Sum
#from django.views.generic import TemplateView

# Create your views here.
#class FigureIndexView(TemplateView):
	#template_name = 'figure/figure_index.html'

# Filter based on division name


def figure_index_view(request):
	# Get all class objects
	figure_overview_data = FigureOverview.objects.all()


	# Filter based on division name
	#kch_data = planting_figure_data.filter(planting_division__division_name__icontains="Kuching").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	return render(request, 'figure/figure_index.html', {
			'figure_overview_data':figure_overview_data,
		})

