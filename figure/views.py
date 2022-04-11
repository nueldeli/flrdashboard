from django.shortcuts import render
from .models import FigureOverview, PlantingFigure
from django.db.models import Sum
#from django.views.generic import TemplateView

# Create your views here.
#class FigureIndexView(TemplateView):
	#template_name = 'figure/figure_index.html'

# Filter based on division name


def figure_index_view(request):
	# Get all class objects
	figure_overview_data = FigureOverview.objects.all()
	planting_figure_data = PlantingFigure.objects.all()
	# Filter based on division name
	kch_data = planting_figure_data.filter(planting_division__division_name__icontains="Kuching").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_data = PlantingFigure.objects.filter(planting_division__division_name__icontains="Sarikei").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_data = PlantingFigure.objects.filter(planting_division__division_name__icontains="Kapit").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_data = PlantingFigure.objects.filter(planting_division__division_name__icontains="Sibu").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_data = PlantingFigure.objects.filter(planting_division__division_name__icontains="Bintulu").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_data = PlantingFigure.objects.filter(planting_division__division_name__icontains="Miri").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_data = PlantingFigure.objects.filter(planting_division__division_name__icontains="Lawas").aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	
	return render(request, 'figure/figure_index.html', {
			'figure_overview_data':figure_overview_data,
			'planting_figure_data':planting_figure_data,
			'kch_data':kch_data,
			
		})

