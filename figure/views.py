from django.shortcuts import render
from .models import FigureOverview, FigureByDivision

def figure_index_view(request):
	fo_data_object = FigureOverview.objects.all()
	fd_queryset = FigureByDivision.objects.all()
	label = []
	div_data = []

	for division in fd_queryset:
		label.append(division.division_name)
		div_data.append(division.division_total_trees)

	return render(request, 'figure/figure_index.html', {
			'fo_data_object':fo_data_object,
			'fd_queryset':fd_queryset,
			'label':label,
			'div_data':div_data
		})