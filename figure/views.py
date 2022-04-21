from django.shortcuts import render
import math
from django.db.models import Sum
from .models import FigureOverview, FigureByDivision, PlantingFigure

fo_data_object = FigureOverview.objects.all()
fd_queryset = FigureByDivision.objects.all() 
pf_queryset = PlantingFigure.objects.all()

def figure_index_view(request):
	label = []
	div_data = []
	div_percentage_data = []

	for division in fd_queryset:
		label.append(division.division_name)
		div_data.append(division.division_total_trees)

	fd_total = sum(div_data)

	for i in fd_queryset:
		a = math.trunc((i.division_total_trees / fd_total) * 100)
		div_percentage_data.append(a) 

	return render(request, 'figure/figure_index.html', {
			'fo_data_object':fo_data_object,
			'fd_queryset':fd_queryset,
			'label':label,
			'div_data':div_data,
			'div_percentage_data':div_percentage_data
		})

def kuching_index_view(request):
	kch_pf_object = pf_queryset.filter(planting_division__icontains='Kuching')
	kch_fd_object = fd_queryset.filter(division_name__icontains='Kuching')
	kch_pf_cumulative = pf_queryset.filter(planting_division__icontains='Kuching').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_pf_total_species = pf_queryset.filter(planting_number_of_species__icontains='Kuching').aggregate(Sum('planting_number_of_species'))['planting_number_of_species__sum']
	return render(request, 'figure/kuching_index.html', {
		'kch_pf_object':kch_pf_object,
		'kch_fd_object':kch_fd_object,
		'kch_pf_cumulative':kch_pf_cumulative,
		'kch_pf_total_species':kch_pf_total_species
		})





