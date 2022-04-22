from django.shortcuts import render
import math
from django.db.models import Sum
from django.views.generic import DetailView
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

### ALL DIVISION-RELATED

# KUCHING
def kuching_index_view(request):
	return render(request, 'figure/kuching_index.html')

def kuching_2021_view(request):
	kch_pf_object = pf_queryset.filter(planting_division__icontains='Kuching')
	kch_fd_object = fd_queryset.filter(division_name__icontains='Kuching')

	kch_2021 = kch_pf_object.filter(year__icontains='2021')
	kch_2021_cumulative = kch_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2021_january = kch_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_february = kch_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_march = kch_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_april = kch_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_may = kch_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_june = kch_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_july = kch_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_august = kch_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_september = kch_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_october = kch_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_november = kch_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2021_disember = kch_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kch_2021_data = [kch_2021_january, kch_2021_february, kch_2021_march, kch_2021_april,
	kch_2021_may, kch_2021_june, kch_2021_july, kch_2021_august, kch_2021_september, 
	kch_2021_october, kch_2021_november, kch_2021_disember]

	return render(request, 'figure/_include/2021/kuching_2021.html', {
		'kch_2021':kch_2021,
		'kch_fd_object':kch_fd_object,
		'kch_2021_cumulative':kch_2021_cumulative,
		'kch_2021_label':kch_2021_label,
		'kch_2021_data':kch_2021_data,
		})	

def kuching_2022_view(request):
	kch_pf_object = pf_queryset.filter(planting_division__icontains='Kuching')
	kch_fd_object = fd_queryset.filter(division_name__icontains='Kuching')

	
	kch_2022 = kch_pf_object.filter(year__icontains='2022')
	kch_2022_cumulative = kch_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	
	kch_2022_january = kch_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_february = kch_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_march = kch_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_april = kch_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_may = kch_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_june = kch_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_july = kch_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_august = kch_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_september = kch_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_october = kch_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_november = kch_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2022_disember = kch_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kch_2022_data = [kch_2022_january, kch_2022_february, kch_2022_march, kch_2022_april,
	kch_2022_may, kch_2022_june, kch_2022_july, kch_2022_august, kch_2022_september, 
	kch_2022_october, kch_2022_november, kch_2022_disember]

	return render(request, 'figure/_include/2022/kuching_2022.html', {
		'kch_2022':kch_2022,
		'kch_fd_object':kch_fd_object,
		'kch_2022_cumulative':kch_2022_cumulative,
		'kch_2022_label':kch_2022_label,
		'kch_2022_data':kch_2022_data,
		})

def kuching_2023_view(request):
	kch_pf_object = pf_queryset.filter(planting_division__icontains='Kuching')
	kch_fd_object = fd_queryset.filter(division_name__icontains='Kuching')

	kch_2023 = kch_pf_object.filter(year__icontains='2023')
	kch_2023_cumulative = kch_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2023_january = kch_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_february = kch_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_march = kch_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_april = kch_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_may = kch_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_june = kch_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_july = kch_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_august = kch_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_september = kch_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_october = kch_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_november = kch_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2023_disember = kch_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kch_2023_data = [kch_2023_january, kch_2023_february, kch_2023_march, kch_2023_april,
	kch_2023_may, kch_2023_june, kch_2023_july, kch_2023_august, kch_2023_september, 
	kch_2023_october, kch_2023_november, kch_2023_disember]

	return render(request, 'figure/_include/2023/kuching_2023.html', {
		'kch_2023':kch_2023,
		'kch_fd_object':kch_fd_object,
		'kch_2023_cumulative':kch_2023_cumulative,
		'kch_2023_label':kch_2023_label,
		'kch_2023_data':kch_2023_data,
		})

def kuching_2024_view(request):
	kch_pf_object = pf_queryset.filter(planting_division__icontains='Kuching')
	kch_fd_object = fd_queryset.filter(division_name__icontains='Kuching')

	kch_2024 = kch_pf_object.filter(year__icontains='2024')
	kch_2024_cumulative = kch_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2024_january = kch_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_february = kch_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_march = kch_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_april = kch_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_may = kch_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_june = kch_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_july = kch_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_august = kch_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_september = kch_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_october = kch_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_november = kch_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2024_disember = kch_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kch_2024_data = [kch_2024_january, kch_2024_february, kch_2024_march, kch_2024_april,
	kch_2024_may, kch_2024_june, kch_2024_july, kch_2024_august, kch_2024_september, 
	kch_2024_october, kch_2024_november, kch_2024_disember]

	return render(request, 'figure/_include/2024/kuching_2024.html', {
		'kch_2024':kch_2024,
		'kch_fd_object':kch_fd_object,
		'kch_2024_cumulative':kch_2024_cumulative,
		'kch_2024_label':kch_2024_label,
		'kch_2024_data':kch_2024_data,
		})

def kuching_2025_view(request):
	kch_pf_object = pf_queryset.filter(planting_division__icontains='Kuching')
	kch_fd_object = fd_queryset.filter(division_name__icontains='Kuching')

	kch_2025 = kch_pf_object.filter(year__icontains='2024')
	kch_2025_cumulative = kch_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	
	kch_2025_january = kch_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_february = kch_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_march = kch_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_april = kch_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_may = kch_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_june = kch_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_july = kch_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_august = kch_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_september = kch_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_october = kch_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_november = kch_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kch_2025_disember = kch_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kch_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kch_2025_data = [kch_2025_january, kch_2025_february, kch_2025_march, kch_2025_april,
	kch_2025_may, kch_2025_june, kch_2025_july, kch_2025_august, kch_2025_september, 
	kch_2025_october, kch_2025_november, kch_2025_disember]

	return render(request, 'figure/_include/2025/kuching_2025.html', {
		'kch_2025':kch_2025,
		'kch_fd_object':kch_fd_object,
		'kch_2025_cumulative':kch_2025_cumulative,
		'kch_2025_label':kch_2025_label,
		'kch_2025_data':kch_2025_data,
		})

# SRI AMAN
def sri_aman_index_view(request):
	return render(request, 'figure/sri_aman_index.html')

def sri_aman_2021_view(request):
	sa_pf_object = pf_queryset.filter(planting_division__icontains='Sri Aman')
	sa_fd_object = fd_queryset.filter(division_name__icontains='Sri Aman')

	sa_2021 = sa_pf_object.filter(year__icontains='2021')
	sa_2021_cumulative = sa_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2021_january = sa_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_february = sa_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_march = sa_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_april = sa_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_may = sa_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_june = sa_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_july = sa_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_august = sa_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_september = sa_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_october = sa_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_november = sa_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2021_disember = sa_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sa_2021_data = [sa_2021_january, sa_2021_february, sa_2021_march, sa_2021_april,
	sa_2021_may, sa_2021_june, sa_2021_july, sa_2021_august, sa_2021_september, 
	sa_2021_october, sa_2021_november, sa_2021_disember]

	return render(request, 'figure/_include/2021/sri_aman_2021.html', {
		'sa_2021':sa_2021,
		'sa_fd_object':sa_fd_object,
		'sa_2021_cumulative':sa_2021_cumulative,
		'sa_2021_label':sa_2021_label,
		'sa_2021_data':sa_2021_data,
		})
def sri_aman_2022_view(request):
	sa_pf_object = pf_queryset.filter(planting_division__icontains='Sri Aman')
	sa_fd_object = fd_queryset.filter(division_name__icontains='Sri Aman')

	sa_2022 = sa_pf_object.filter(year__icontains='2022')
	sa_2022_cumulative = sa_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2022_january = sa_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_february = sa_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_march = sa_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_april = sa_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_may = sa_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_june = sa_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_july = sa_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_august = sa_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_september = sa_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_october = sa_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_november = sa_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2022_disember = sa_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sa_2022_data = [sa_2022_january, sa_2022_february, sa_2022_march, sa_2022_april,
	sa_2022_may, sa_2022_june, sa_2022_july, sa_2022_august, sa_2022_september, 
	sa_2022_october, sa_2022_november, sa_2022_disember]

	return render(request, 'figure/_include/2022/sri_aman_2022.html', {
		'sa_2022':sa_2022,
		'sa_fd_object':sa_fd_object,
		'sa_2022_cumulative':sa_2022_cumulative,
		'sa_2022_label':sa_2022_label,
		'sa_2022_data':sa_2022_data,
		})

def sri_aman_2023_view(request):
	sa_pf_object = pf_queryset.filter(planting_division__icontains='Sri Aman')
	sa_fd_object = fd_queryset.filter(division_name__icontains='Sri Aman')

	sa_2023 = sa_pf_object.filter(year__icontains='2023')
	sa_2023_cumulative = sa_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2023_january = sa_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_february = sa_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_march = sa_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_april = sa_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_may = sa_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_june = sa_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_july = sa_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_august = sa_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_september = sa_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_october = sa_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_november = sa_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2023_disember = sa_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sa_2023_data = [sa_2023_january, sa_2023_february, sa_2023_march, sa_2023_april,
	sa_2023_may, sa_2023_june, sa_2023_july, sa_2023_august, sa_2023_september, 
	sa_2023_october, sa_2023_november, sa_2023_disember]

	return render(request, 'figure/_include/2023/sri_aman_2023.html', {
		'sa_2023':sa_2023,
		'sa_fd_object':sa_fd_object,
		'sa_2023_cumulative':sa_2023_cumulative,
		'sa_2023_label':sa_2023_label,
		'sa_2023_data':sa_2023_data,
		})

def sri_aman_2024_view(request):
	sa_pf_object = pf_queryset.filter(planting_division__icontains='Sri Aman')
	sa_fd_object = fd_queryset.filter(division_name__icontains='Sri Aman')

	sa_2024 = sa_pf_object.filter(year__icontains='2024')
	sa_2024_cumulative = sa_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2024_january = sa_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_february = sa_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_march = sa_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_april = sa_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_may = sa_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_june = sa_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_july = sa_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_august = sa_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_september = sa_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_october = sa_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_november = sa_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2024_disember = sa_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sa_2024_data = [sa_2024_january, sa_2024_february, sa_2024_march, sa_2024_april,
	sa_2024_may, sa_2024_june, sa_2024_july, sa_2024_august, sa_2024_september, 
	sa_2024_october, sa_2024_november, sa_2024_disember]

	return render(request, 'figure/_include/2024/sri_aman_2024.html', {
		'sa_2024':sa_2024,
		'sa_fd_object':sa_fd_object,
		'sa_2024_cumulative':sa_2024_cumulative,
		'sa_2024_label':sa_2024_label,
		'sa_2024_data':sa_2024_data,
		})

def sri_aman_2025_view(request):
	sa_pf_object = pf_queryset.filter(planting_division__icontains='Sri Aman')
	sa_fd_object = fd_queryset.filter(division_name__icontains='Sri Aman')

	sa_2025 = sa_pf_object.filter(year__icontains='2025')
	sa_2025_cumulative = sa_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2025_january = sa_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_february = sa_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_march = sa_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_april = sa_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_may = sa_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_june = sa_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_july = sa_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_august = sa_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_september = sa_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_october = sa_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_november = sa_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sa_2025_disember = sa_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sa_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sa_2025_data = [sa_2025_january, sa_2025_february, sa_2025_march, sa_2025_april,
	sa_2025_may, sa_2025_june, sa_2025_july, sa_2025_august, sa_2025_september, 
	sa_2025_october, sa_2025_november, sa_2025_disember]

	return render(request, 'figure/_include/2025/sri_aman_2025.html', {
		'sa_2025':sa_2025,
		'sa_fd_object':sa_fd_object,
		'sa_2025_cumulative':sa_2025_cumulative,
		'sa_2025_label':sa_2025_label,
		'sa_2025_data':sa_2025_data,
		})

# SARIKEI

class PlantingFigureDetailView(DetailView):
	model = PlantingFigure
	template_name = 'figure/division_detail.html'