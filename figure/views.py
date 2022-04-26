from django.shortcuts import render
import math
from django.db.models import Sum
from django.views.generic import DetailView, UpdateView
from .models import FigureOverview, FigureByDivision, PlantingFigure
from .forms import UpdateFigureOverviewForm, UpdateKuchingDivisionForm

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

class UpdateFigureOverviewView(UpdateView):
	model = FigureOverview
	template_name = 'figure/figure_overview_update.html'
	form_class = UpdateFigureOverviewForm

class UpdateKuchingDivisionView(UpdateView):
	model = FigureOverview
	template_name = '_include/division_update/kuching_division_update.html'
	form_class = UpdateKuchingDivisionForm

### ALL DIVISION-RELATED

# KUCHING
def kuching_index_view(request):
	kch_fd = fd_queryset.filter(division_name__icontains='Kuching')
	return render(request, 'figure/kuching_index.html', {'kch_fd':kch_fd})

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
def sarikei_index_view(request):
	return render(request, 'figure/sarikei_index.html')

def sarikei_2021_view(request):
	srk_pf_object = pf_queryset.filter(planting_division__icontains='Sarikei')
	srk_fd_object = fd_queryset.filter(division_name__icontains='Sarikei')

	srk_2021 = srk_pf_object.filter(year__icontains='2021')
	srk_2021_cumulative = srk_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2021_january = srk_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_february = srk_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_march = srk_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_april = srk_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_may = srk_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_june = srk_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_july = srk_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_august = srk_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_september = srk_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_october = srk_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_november = srk_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2021_disember = srk_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	srk_2021_data = [srk_2021_january, srk_2021_february, srk_2021_march, srk_2021_april,
	srk_2021_may, srk_2021_june, srk_2021_july, srk_2021_august, srk_2021_september, 
	srk_2021_october, srk_2021_november, srk_2021_disember]

	return render(request, 'figure/_include/2021/sarikei_2021.html', {
		'srk_2021':srk_2021,
		'srk_fd_object':srk_fd_object,
		'srk_2021_cumulative':srk_2021_cumulative,
		'srk_2021_label':srk_2021_label,
		'srk_2021_data':srk_2021_data,
		})

def sarikei_2022_view(request):
	srk_pf_object = pf_queryset.filter(planting_division__icontains='Sarikei')
	srk_fd_object = fd_queryset.filter(division_name__icontains='Sarikei')

	srk_2022 = srk_pf_object.filter(year__icontains='2022')
	srk_2022_cumulative = srk_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2022_january = srk_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_february = srk_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_march = srk_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_april = srk_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_may = srk_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_june = srk_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_july = srk_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_august = srk_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_september = srk_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_october = srk_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_november = srk_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2022_disember = srk_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	srk_2022_data = [srk_2022_january, srk_2022_february, srk_2022_march, srk_2022_april,
	srk_2022_may, srk_2022_june, srk_2022_july, srk_2022_august, srk_2022_september, 
	srk_2022_october, srk_2022_november, srk_2022_disember]

	return render(request, 'figure/_include/2022/sarikei_2022.html', {
		'srk_2022':srk_2022,
		'srk_fd_object':srk_fd_object,
		'srk_2022_cumulative':srk_2022_cumulative,
		'srk_2022_label':srk_2022_label,
		'srk_2022_data':srk_2022_data,
		})

def sarikei_2023_view(request):
	srk_pf_object = pf_queryset.filter(planting_division__icontains='Sarikei')
	srk_fd_object = fd_queryset.filter(division_name__icontains='Sarikei')

	srk_2023 = srk_pf_object.filter(year__icontains='2023')
	srk_2023_cumulative = srk_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2023_january = srk_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_february = srk_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_march = srk_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_april = srk_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_may = srk_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_june = srk_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_july = srk_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_august = srk_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_september = srk_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_october = srk_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_november = srk_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2023_disember = srk_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	srk_2023_data = [srk_2023_january, srk_2023_february, srk_2023_march, srk_2023_april,
	srk_2023_may, srk_2023_june, srk_2023_july, srk_2023_august, srk_2023_september, 
	srk_2023_october, srk_2023_november, srk_2023_disember]

	return render(request, 'figure/_include/2023/sarikei_2023.html', {
		'srk_2023':srk_2023,
		'srk_fd_object':srk_fd_object,
		'srk_2023_cumulative':srk_2023_cumulative,
		'srk_2023_label':srk_2023_label,
		'srk_2023_data':srk_2023_data,
		})

def sarikei_2024_view(request):
	srk_pf_object = pf_queryset.filter(planting_division__icontains='Sarikei')
	srk_fd_object = fd_queryset.filter(division_name__icontains='Sarikei')

	srk_2024 = srk_pf_object.filter(year__icontains='2024')
	srk_2024_cumulative = srk_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2024_january = srk_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_february = srk_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_march = srk_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_april = srk_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_may = srk_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_june = srk_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_july = srk_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_august = srk_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_september = srk_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_october = srk_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_november = srk_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2024_disember = srk_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	srk_2024_data = [srk_2024_january, srk_2024_february, srk_2024_march, srk_2024_april,
	srk_2024_may, srk_2024_june, srk_2024_july, srk_2024_august, srk_2024_september, 
	srk_2024_october, srk_2024_november, srk_2024_disember]

	return render(request, 'figure/_include/2024/sarikei_2024.html', {
		'srk_2024':srk_2024,
		'srk_fd_object':srk_fd_object,
		'srk_2024_cumulative':srk_2024_cumulative,
		'srk_2024_label':srk_2024_label,
		'srk_2024_data':srk_2024_data,
		})

def sarikei_2025_view(request):
	srk_pf_object = pf_queryset.filter(planting_division__icontains='Sarikei')
	srk_fd_object = fd_queryset.filter(division_name__icontains='Sarikei')

	srk_2025 = srk_pf_object.filter(year__icontains='2025')
	srk_2025_cumulative = srk_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2025_january = srk_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_february = srk_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_march = srk_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_april = srk_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_may = srk_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_june = srk_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_july = srk_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_august = srk_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_september = srk_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_october = srk_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_november = srk_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	srk_2025_disember = srk_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	srk_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	srk_2025_data = [srk_2025_january, srk_2025_february, srk_2025_march, srk_2025_april,
	srk_2025_may, srk_2025_june, srk_2025_july, srk_2025_august, srk_2025_september, 
	srk_2025_october, srk_2025_november, srk_2025_disember]

	return render(request, 'figure/_include/2025/sarikei_2025.html', {
		'srk_2025':srk_2025,
		'srk_fd_object':srk_fd_object,
		'srk_2025_cumulative':srk_2025_cumulative,
		'srk_2025_label':srk_2025_label,
		'srk_2025_data':srk_2025_data,
		})

# KAPIT
def kapit_index_view(request):
	return render(request, 'figure/kapit_index.html')

def kapit_2021_view(request):
	kpt_pf_object = pf_queryset.filter(planting_division__icontains='Kapit')
	kpt_fd_object = fd_queryset.filter(division_name__icontains='Kapit')

	kpt_2021 = kpt_pf_object.filter(year__icontains='2021')
	kpt_2021_cumulative = kpt_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2021_january = kpt_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_february = kpt_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_march = kpt_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_april = kpt_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_may = kpt_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_june = kpt_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_july = kpt_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_august = kpt_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_september = kpt_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_october = kpt_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_november = kpt_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2021_disember = kpt_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kpt_2021_data = [kpt_2021_january, kpt_2021_february, kpt_2021_march, kpt_2021_april,
	kpt_2021_may, kpt_2021_june, kpt_2021_july, kpt_2021_august, kpt_2021_september, 
	kpt_2021_october, kpt_2021_november, kpt_2021_disember]

	return render(request, 'figure/_include/2021/kapit_2021.html', {
		'kpt_2021':kpt_2021,
		'kpt_fd_object':kpt_fd_object,
		'kpt_2021_cumulative':kpt_2021_cumulative,
		'kpt_2021_label':kpt_2021_label,
		'kpt_2021_data':kpt_2021_data,
		})

def kapit_2022_view(request):
	kpt_pf_object = pf_queryset.filter(planting_division__icontains='Kapit')
	kpt_fd_object = fd_queryset.filter(division_name__icontains='Kapit')

	kpt_2022 = kpt_pf_object.filter(year__icontains='2022')
	kpt_2022_cumulative = kpt_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2022_january = kpt_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_february = kpt_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_march = kpt_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_april = kpt_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_may = kpt_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_june = kpt_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_july = kpt_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_august = kpt_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_september = kpt_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_october = kpt_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_november = kpt_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2022_disember = kpt_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kpt_2022_data = [kpt_2022_january, kpt_2022_february, kpt_2022_march, kpt_2022_april,
	kpt_2022_may, kpt_2022_june, kpt_2022_july, kpt_2022_august, kpt_2022_september, 
	kpt_2022_october, kpt_2022_november, kpt_2022_disember]

	return render(request, 'figure/_include/2022/kapit_2022.html', {
		'kpt_2022':kpt_2022,
		'kpt_fd_object':kpt_fd_object,
		'kpt_2022_cumulative':kpt_2022_cumulative,
		'kpt_2022_label':kpt_2022_label,
		'kpt_2022_data':kpt_2022_data,
		})

def kapit_2023_view(request):
	kpt_pf_object = pf_queryset.filter(planting_division__icontains='Kapit')
	kpt_fd_object = fd_queryset.filter(division_name__icontains='Kapit')

	kpt_2023 = kpt_pf_object.filter(year__icontains='2023')
	kpt_2023_cumulative = kpt_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2023_january = kpt_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_february = kpt_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_march = kpt_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_april = kpt_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_may = kpt_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_june = kpt_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_july = kpt_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_august = kpt_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_september = kpt_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_october = kpt_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_november = kpt_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2023_disember = kpt_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kpt_2023_data = [kpt_2023_january, kpt_2023_february, kpt_2023_march, kpt_2023_april,
	kpt_2023_may, kpt_2023_june, kpt_2023_july, kpt_2023_august, kpt_2023_september, 
	kpt_2023_october, kpt_2023_november, kpt_2023_disember]

	return render(request, 'figure/_include/2023/kapit_2023.html', {
		'kpt_2023':kpt_2023,
		'kpt_fd_object':kpt_fd_object,
		'kpt_2023_cumulative':kpt_2023_cumulative,
		'kpt_2023_label':kpt_2023_label,
		'kpt_2023_data':kpt_2023_data,
		})

def kapit_2024_view(request):
	kpt_pf_object = pf_queryset.filter(planting_division__icontains='Kapit')
	kpt_fd_object = fd_queryset.filter(division_name__icontains='Kapit')

	kpt_2024 = kpt_pf_object.filter(year__icontains='2024')
	kpt_2024_cumulative = kpt_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2024_january = kpt_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_february = kpt_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_march = kpt_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_april = kpt_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_may = kpt_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_june = kpt_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_july = kpt_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_august = kpt_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_september = kpt_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_october = kpt_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_november = kpt_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2024_disember = kpt_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kpt_2024_data = [kpt_2024_january, kpt_2024_february, kpt_2024_march, kpt_2024_april,
	kpt_2024_may, kpt_2024_june, kpt_2024_july, kpt_2024_august, kpt_2024_september, 
	kpt_2024_october, kpt_2024_november, kpt_2024_disember]

	return render(request, 'figure/_include/2024/kapit_2024.html', {
		'kpt_2024':kpt_2024,
		'kpt_fd_object':kpt_fd_object,
		'kpt_2024_cumulative':kpt_2024_cumulative,
		'kpt_2024_label':kpt_2024_label,
		'kpt_2024_data':kpt_2024_data,
		})

def kapit_2025_view(request):
	kpt_pf_object = pf_queryset.filter(planting_division__icontains='Kapit')
	kpt_fd_object = fd_queryset.filter(division_name__icontains='Kapit')

	kpt_2025 = kpt_pf_object.filter(year__icontains='2025')
	kpt_2025_cumulative = kpt_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2025_january = kpt_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_february = kpt_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_march = kpt_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_april = kpt_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_may = kpt_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_june = kpt_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_july = kpt_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_august = kpt_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_september = kpt_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_october = kpt_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_november = kpt_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	kpt_2025_disember = kpt_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	kpt_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	kpt_2025_data = [kpt_2025_january, kpt_2025_february, kpt_2025_march, kpt_2025_april,
	kpt_2025_may, kpt_2025_june, kpt_2025_july, kpt_2025_august, kpt_2025_september, 
	kpt_2025_october, kpt_2025_november, kpt_2025_disember]

	return render(request, 'figure/_include/2025/kapit_2025.html', {
		'kpt_2025':kpt_2025,
		'kpt_fd_object':kpt_fd_object,
		'kpt_2025_cumulative':kpt_2025_cumulative,
		'kpt_2025_label':kpt_2025_label,
		'kpt_2025_data':kpt_2025_data,
		})

# SIBU
def sibu_index_view(request):
	return render(request, 'figure/sibu_index.html')

def sibu_2021_view(request):
	sbu_pf_object = pf_queryset.filter(planting_division__icontains='Sibu')
	sbu_fd_object = fd_queryset.filter(division_name__icontains='Sibu')

	sbu_2021 = sbu_pf_object.filter(year__icontains='2021')
	sbu_2021_cumulative = sbu_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2021_january = sbu_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_february = sbu_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_march = sbu_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_april = sbu_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_may = sbu_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_june = sbu_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_july = sbu_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_august = sbu_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_september = sbu_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_october = sbu_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_november = sbu_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2021_disember = sbu_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sbu_2021_data = [sbu_2021_january, sbu_2021_february, sbu_2021_march, sbu_2021_april,
	sbu_2021_may, sbu_2021_june, sbu_2021_july, sbu_2021_august, sbu_2021_september, 
	sbu_2021_october, sbu_2021_november, sbu_2021_disember]

	return render(request, 'figure/_include/2021/sibu_2021.html', {
		'sbu_2021':sbu_2021,
		'sbu_fd_object':sbu_fd_object,
		'sbu_2021_cumulative':sbu_2021_cumulative,
		'sbu_2021_label':sbu_2021_label,
		'sbu_2021_data':sbu_2021_data,
		})

def sibu_2022_view(request):
	sbu_pf_object = pf_queryset.filter(planting_division__icontains='Sibu')
	sbu_fd_object = fd_queryset.filter(division_name__icontains='Sibu')

	sbu_2022 = sbu_pf_object.filter(year__icontains='2022')
	sbu_2022_cumulative = sbu_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2022_january = sbu_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_february = sbu_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_march = sbu_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_april = sbu_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_may = sbu_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_june = sbu_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_july = sbu_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_august = sbu_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_september = sbu_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_october = sbu_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_november = sbu_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2022_disember = sbu_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sbu_2022_data = [sbu_2022_january, sbu_2022_february, sbu_2022_march, sbu_2022_april,
	sbu_2022_may, sbu_2022_june, sbu_2022_july, sbu_2022_august, sbu_2022_september, 
	sbu_2022_october, sbu_2022_november, sbu_2022_disember]

	return render(request, 'figure/_include/2022/sibu_2022.html', {
		'sbu_2022':sbu_2022,
		'sbu_fd_object':sbu_fd_object,
		'sbu_2022_cumulative':sbu_2022_cumulative,
		'sbu_2022_label':sbu_2022_label,
		'sbu_2022_data':sbu_2022_data,
		})

def sibu_2023_view(request):
	sbu_pf_object = pf_queryset.filter(planting_division__icontains='Sibu')
	sbu_fd_object = fd_queryset.filter(division_name__icontains='Sibu')

	sbu_2023 = sbu_pf_object.filter(year__icontains='2023')
	sbu_2023_cumulative = sbu_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2023_january = sbu_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_february = sbu_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_march = sbu_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_april = sbu_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_may = sbu_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_june = sbu_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_july = sbu_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_august = sbu_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_september = sbu_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_october = sbu_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_november = sbu_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2023_disember = sbu_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sbu_2023_data = [sbu_2023_january, sbu_2023_february, sbu_2023_march, sbu_2023_april,
	sbu_2023_may, sbu_2023_june, sbu_2023_july, sbu_2023_august, sbu_2023_september, 
	sbu_2023_october, sbu_2023_november, sbu_2023_disember]

	return render(request, 'figure/_include/2023/sibu_2023.html', {
		'sbu_2023':sbu_2023,
		'sbu_fd_object':sbu_fd_object,
		'sbu_2023_cumulative':sbu_2023_cumulative,
		'sbu_2023_label':sbu_2023_label,
		'sbu_2023_data':sbu_2023_data,
		})

def sibu_2024_view(request):
	sbu_pf_object = pf_queryset.filter(planting_division__icontains='Sibu')
	sbu_fd_object = fd_queryset.filter(division_name__icontains='Sibu')

	sbu_2024 = sbu_pf_object.filter(year__icontains='2024')
	sbu_2024_cumulative = sbu_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2024_january = sbu_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_february = sbu_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_march = sbu_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_april = sbu_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_may = sbu_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_june = sbu_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_july = sbu_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_august = sbu_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_september = sbu_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_october = sbu_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_november = sbu_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2024_disember = sbu_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sbu_2024_data = [sbu_2024_january, sbu_2024_february, sbu_2024_march, sbu_2024_april,
	sbu_2024_may, sbu_2024_june, sbu_2024_july, sbu_2024_august, sbu_2024_september, 
	sbu_2024_october, sbu_2024_november, sbu_2024_disember]

	return render(request, 'figure/_include/2024/sibu_2024.html', {
		'sbu_2024':sbu_2024,
		'sbu_fd_object':sbu_fd_object,
		'sbu_2024_cumulative':sbu_2024_cumulative,
		'sbu_2024_label':sbu_2024_label,
		'sbu_2024_data':sbu_2024_data,
		})

def sibu_2025_view(request):
	sbu_pf_object = pf_queryset.filter(planting_division__icontains='Sibu')
	sbu_fd_object = fd_queryset.filter(division_name__icontains='Sibu')

	sbu_2025 = sbu_pf_object.filter(year__icontains='2025')
	sbu_2025_cumulative = sbu_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2025_january = sbu_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_february = sbu_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_march = sbu_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_april = sbu_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_may = sbu_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_june = sbu_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_july = sbu_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_august = sbu_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_september = sbu_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_october = sbu_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_november = sbu_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	sbu_2025_disember = sbu_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	sbu_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	sbu_2025_data = [sbu_2025_january, sbu_2025_february, sbu_2025_march, sbu_2025_april,
	sbu_2025_may, sbu_2025_june, sbu_2025_july, sbu_2025_august, sbu_2025_september, 
	sbu_2025_october, sbu_2025_november, sbu_2025_disember]

	return render(request, 'figure/_include/2025/sibu_2025.html', {
		'sbu_2025':sbu_2025,
		'sbu_fd_object':sbu_fd_object,
		'sbu_2025_cumulative':sbu_2025_cumulative,
		'sbu_2025_label':sbu_2025_label,
		'sbu_2025_data':sbu_2025_data,
		})

# BINTULU
def bintulu_index_view(request):
	return render(request, 'figure/bintulu_index.html')

def bintulu_2021_view(request):
	btu_pf_object = pf_queryset.filter(planting_division__icontains='Bintulu')
	btu_fd_object = fd_queryset.filter(division_name__icontains='Bintulu')

	btu_2021 = btu_pf_object.filter(year__icontains='2021')
	btu_2021_cumulative = btu_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2021_january = btu_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_february = btu_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_march = btu_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_april = btu_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_may = btu_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_june = btu_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_july = btu_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_august = btu_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_september = btu_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_october = btu_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_november = btu_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2021_disember = btu_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	btu_2021_data = [btu_2021_january, btu_2021_february, btu_2021_march, btu_2021_april,
	btu_2021_may, btu_2021_june, btu_2021_july, btu_2021_august, btu_2021_september, 
	btu_2021_october, btu_2021_november, btu_2021_disember]

	return render(request, 'figure/_include/2021/bintulu_2021.html', {
		'btu_2021':btu_2021,
		'btu_fd_object':btu_fd_object,
		'btu_2021_cumulative':btu_2021_cumulative,
		'btu_2021_label':btu_2021_label,
		'btu_2021_data':btu_2021_data,
		})

def bintulu_2022_view(request):
	btu_pf_object = pf_queryset.filter(planting_division__icontains='Bintulu')
	btu_fd_object = fd_queryset.filter(division_name__icontains='Bintulu')

	btu_2022 = btu_pf_object.filter(year__icontains='2022')
	btu_2022_cumulative = btu_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2022_january = btu_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_february = btu_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_march = btu_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_april = btu_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_may = btu_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_june = btu_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_july = btu_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_august = btu_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_september = btu_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_october = btu_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_november = btu_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2022_disember = btu_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	btu_2022_data = [btu_2022_january, btu_2022_february, btu_2022_march, btu_2022_april,
	btu_2022_may, btu_2022_june, btu_2022_july, btu_2022_august, btu_2022_september, 
	btu_2022_october, btu_2022_november, btu_2022_disember]

	return render(request, 'figure/_include/2022/bintulu_2022.html', {
		'btu_2022':btu_2022,
		'btu_fd_object':btu_fd_object,
		'btu_2022_cumulative':btu_2022_cumulative,
		'btu_2022_label':btu_2022_label,
		'btu_2022_data':btu_2022_data,
		})

def bintulu_2023_view(request):
	btu_pf_object = pf_queryset.filter(planting_division__icontains='Bintulu')
	btu_fd_object = fd_queryset.filter(division_name__icontains='Bintulu')

	btu_2023 = btu_pf_object.filter(year__icontains='2023')
	btu_2023_cumulative = btu_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2023_january = btu_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_february = btu_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_march = btu_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_april = btu_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_may = btu_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_june = btu_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_july = btu_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_august = btu_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_september = btu_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_october = btu_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_november = btu_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2023_disember = btu_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	btu_2023_data = [btu_2023_january, btu_2023_february, btu_2023_march, btu_2023_april,
	btu_2023_may, btu_2023_june, btu_2023_july, btu_2023_august, btu_2023_september, 
	btu_2023_october, btu_2023_november, btu_2023_disember]

	return render(request, 'figure/_include/2023/bintulu_2023.html', {
		'btu_2023':btu_2023,
		'btu_fd_object':btu_fd_object,
		'btu_2023_cumulative':btu_2023_cumulative,
		'btu_2023_label':btu_2023_label,
		'btu_2023_data':btu_2023_data,
		})

def bintulu_2024_view(request):
	btu_pf_object = pf_queryset.filter(planting_division__icontains='Bintulu')
	btu_fd_object = fd_queryset.filter(division_name__icontains='Bintulu')

	btu_2024 = btu_pf_object.filter(year__icontains='2024')
	btu_2024_cumulative = btu_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2024_january = btu_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_february = btu_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_march = btu_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_april = btu_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_may = btu_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_june = btu_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_july = btu_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_august = btu_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_september = btu_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_october = btu_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_november = btu_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2024_disember = btu_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	btu_2024_data = [btu_2024_january, btu_2024_february, btu_2024_march, btu_2024_april,
	btu_2024_may, btu_2024_june, btu_2024_july, btu_2024_august, btu_2024_september, 
	btu_2024_october, btu_2024_november, btu_2024_disember]

	return render(request, 'figure/_include/2024/bintulu_2024.html', {
		'btu_2024':btu_2024,
		'btu_fd_object':btu_fd_object,
		'btu_2024_cumulative':btu_2024_cumulative,
		'btu_2024_label':btu_2024_label,
		'btu_2024_data':btu_2024_data,
		})

def bintulu_2025_view(request):
	btu_pf_object = pf_queryset.filter(planting_division__icontains='Bintulu')
	btu_fd_object = fd_queryset.filter(division_name__icontains='Bintulu')

	btu_2025 = btu_pf_object.filter(year__icontains='2025')
	btu_2025_cumulative = btu_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2025_january = btu_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_february = btu_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_march = btu_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_april = btu_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_may = btu_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_june = btu_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_july = btu_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_august = btu_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_september = btu_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_october = btu_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_november = btu_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	btu_2025_disember = btu_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	btu_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	btu_2025_data = [btu_2025_january, btu_2025_february, btu_2025_march, btu_2025_april,
	btu_2025_may, btu_2025_june, btu_2025_july, btu_2025_august, btu_2025_september, 
	btu_2025_october, btu_2025_november, btu_2025_disember]

	return render(request, 'figure/_include/2025/bintulu_2025.html', {
		'btu_2025':btu_2025,
		'btu_fd_object':btu_fd_object,
		'btu_2025_cumulative':btu_2025_cumulative,
		'btu_2025_label':btu_2025_label,
		'btu_2025_data':btu_2025_data,
		})

# MIRI
def miri_index_view(request):
	return render(request, 'figure/miri_index.html')

def miri_2021_view(request):
	myy_pf_object = pf_queryset.filter(planting_division__icontains='Miri')
	myy_fd_object = fd_queryset.filter(division_name__icontains='Miri')

	myy_2021 = myy_pf_object.filter(year__icontains='2021')
	myy_2021_cumulative = myy_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2021_january = myy_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_february = myy_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_march = myy_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_april = myy_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_may = myy_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_june = myy_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_july = myy_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_august = myy_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_september = myy_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_october = myy_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_november = myy_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2021_disember = myy_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	myy_2021_data = [myy_2021_january, myy_2021_february, myy_2021_march, myy_2021_april,
	myy_2021_may, myy_2021_june, myy_2021_july, myy_2021_august, myy_2021_september, 
	myy_2021_october, myy_2021_november, myy_2021_disember]

	return render(request, 'figure/_include/2021/miri_2021.html', {
		'myy_2021':myy_2021,
		'myy_fd_object':myy_fd_object,
		'myy_2021_cumulative':myy_2021_cumulative,
		'myy_2021_label':myy_2021_label,
		'myy_2021_data':myy_2021_data,
		})

def miri_2022_view(request):
	myy_pf_object = pf_queryset.filter(planting_division__icontains='Miri')
	myy_fd_object = fd_queryset.filter(division_name__icontains='Miri')

	myy_2022 = myy_pf_object.filter(year__icontains='2022')
	myy_2022_cumulative = myy_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2022_january = myy_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_february = myy_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_march = myy_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_april = myy_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_may = myy_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_june = myy_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_july = myy_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_august = myy_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_september = myy_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_october = myy_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_november = myy_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2022_disember = myy_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	myy_2022_data = [myy_2022_january, myy_2022_february, myy_2022_march, myy_2022_april,
	myy_2022_may, myy_2022_june, myy_2022_july, myy_2022_august, myy_2022_september, 
	myy_2022_october, myy_2022_november, myy_2022_disember]

	return render(request, 'figure/_include/2022/miri_2022.html', {
		'myy_2022':myy_2022,
		'myy_fd_object':myy_fd_object,
		'myy_2022_cumulative':myy_2022_cumulative,
		'myy_2022_label':myy_2022_label,
		'myy_2022_data':myy_2022_data,
		})

def miri_2023_view(request):
	myy_pf_object = pf_queryset.filter(planting_division__icontains='Miri')
	myy_fd_object = fd_queryset.filter(division_name__icontains='Miri')

	myy_2023 = myy_pf_object.filter(year__icontains='2023')
	myy_2023_cumulative = myy_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2023_january = myy_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_february = myy_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_march = myy_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_april = myy_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_may = myy_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_june = myy_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_july = myy_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_august = myy_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_september = myy_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_october = myy_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_november = myy_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2023_disember = myy_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	myy_2023_data = [myy_2023_january, myy_2023_february, myy_2023_march, myy_2023_april,
	myy_2023_may, myy_2023_june, myy_2023_july, myy_2023_august, myy_2023_september, 
	myy_2023_october, myy_2023_november, myy_2023_disember]

	return render(request, 'figure/_include/2023/miri_2023.html', {
		'myy_2023':myy_2023,
		'myy_fd_object':myy_fd_object,
		'myy_2023_cumulative':myy_2023_cumulative,
		'myy_2023_label':myy_2023_label,
		'myy_2023_data':myy_2023_data,
		})

def miri_2024_view(request):
	myy_pf_object = pf_queryset.filter(planting_division__icontains='Miri')
	myy_fd_object = fd_queryset.filter(division_name__icontains='Miri')

	myy_2024 = myy_pf_object.filter(year__icontains='2024')
	myy_2024_cumulative = myy_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2024_january = myy_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_february = myy_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_march = myy_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_april = myy_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_may = myy_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_june = myy_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_july = myy_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_august = myy_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_september = myy_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_october = myy_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_november = myy_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2024_disember = myy_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	myy_2024_data = [myy_2024_january, myy_2024_february, myy_2024_march, myy_2024_april,
	myy_2024_may, myy_2024_june, myy_2024_july, myy_2024_august, myy_2024_september, 
	myy_2024_october, myy_2024_november, myy_2024_disember]

	return render(request, 'figure/_include/2024/miri_2024.html', {
		'myy_2024':myy_2024,
		'myy_fd_object':myy_fd_object,
		'myy_2024_cumulative':myy_2024_cumulative,
		'myy_2024_label':myy_2024_label,
		'myy_2024_data':myy_2024_data,
		})

def miri_2025_view(request):
	myy_pf_object = pf_queryset.filter(planting_division__icontains='Miri')
	myy_fd_object = fd_queryset.filter(division_name__icontains='Miri')

	myy_2025 = myy_pf_object.filter(year__icontains='2025')
	myy_2025_cumulative = myy_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2025_january = myy_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_february = myy_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_march = myy_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_april = myy_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_may = myy_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_june = myy_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_july = myy_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_august = myy_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_september = myy_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_october = myy_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_november = myy_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	myy_2025_disember = myy_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	myy_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	myy_2025_data = [myy_2025_january, myy_2025_february, myy_2025_march, myy_2025_april,
	myy_2025_may, myy_2025_june, myy_2025_july, myy_2025_august, myy_2025_september, 
	myy_2025_october, myy_2025_november, myy_2025_disember]

	return render(request, 'figure/_include/2025/miri_2025.html', {
		'myy_2025':myy_2025,
		'myy_fd_object':myy_fd_object,
		'myy_2025_cumulative':myy_2025_cumulative,
		'myy_2025_label':myy_2025_label,
		'myy_2025_data':myy_2025_data,
		})

# LIMBANG
def limbang_index_view(request):
	return render(request, 'figure/limbang_index.html')

def limbang_2021_view(request):
	lbg_pf_object = pf_queryset.filter(planting_division__icontains='Limbang')
	lbg_fd_object = fd_queryset.filter(division_name__icontains='Limbang')

	lbg_2021 = lbg_pf_object.filter(year__icontains='2021')
	lbg_2021_cumulative = lbg_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2021_january =lbg_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_february = lbg_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_march = lbg_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_april = lbg_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_may = lbg_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_june = lbg_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_july = lbg_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_august = lbg_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_september = lbg_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_october = lbg_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_november = lbg_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2021_disember = lbg_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lbg_2021_data = [lbg_2021_january, lbg_2021_february, lbg_2021_march, lbg_2021_april,
	lbg_2021_may, lbg_2021_june, lbg_2021_july, lbg_2021_august, lbg_2021_september, 
	lbg_2021_october, lbg_2021_november, lbg_2021_disember]

	return render(request, 'figure/_include/2021/limbang_2021.html', {
		'lbg_2021':lbg_2021,
		'lbg_fd_object':lbg_fd_object,
		'lbg_2021_cumulative':lbg_2021_cumulative,
		'lbg_2021_label':lbg_2021_label,
		'lbg_2021_data':lbg_2021_data,
		})

def limbang_2022_view(request):
	lbg_pf_object = pf_queryset.filter(planting_division__icontains='Limbang')
	lbg_fd_object = fd_queryset.filter(division_name__icontains='Limbang')

	lbg_2022 = lbg_pf_object.filter(year__icontains='2022')
	lbg_2022_cumulative = lbg_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2022_january =lbg_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_february = lbg_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_march = lbg_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_april = lbg_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_may = lbg_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_june = lbg_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_july = lbg_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_august = lbg_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_september = lbg_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_october = lbg_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_november = lbg_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2022_disember = lbg_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lbg_2022_data = [lbg_2022_january, lbg_2022_february, lbg_2022_march, lbg_2022_april,
	lbg_2022_may, lbg_2022_june, lbg_2022_july, lbg_2022_august, lbg_2022_september, 
	lbg_2022_october, lbg_2022_november, lbg_2022_disember]

	return render(request, 'figure/_include/2022/limbang_2022.html', {
		'lbg_2022':lbg_2022,
		'lbg_fd_object':lbg_fd_object,
		'lbg_2022_cumulative':lbg_2022_cumulative,
		'lbg_2022_label':lbg_2022_label,
		'lbg_2022_data':lbg_2022_data,
		})

def limbang_2023_view(request):
	lbg_pf_object = pf_queryset.filter(planting_division__icontains='Limbang')
	lbg_fd_object = fd_queryset.filter(division_name__icontains='Limbang')

	lbg_2023 = lbg_pf_object.filter(year__icontains='2023')
	lbg_2023_cumulative = lbg_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2023_january =lbg_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_february = lbg_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_march = lbg_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_april = lbg_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_may = lbg_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_june = lbg_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_july = lbg_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_august = lbg_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_september = lbg_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_october = lbg_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_november = lbg_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2023_disember = lbg_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lbg_2023_data = [lbg_2023_january, lbg_2023_february, lbg_2023_march, lbg_2023_april,
	lbg_2023_may, lbg_2023_june, lbg_2023_july, lbg_2023_august, lbg_2023_september, 
	lbg_2023_october, lbg_2023_november, lbg_2023_disember]

	return render(request, 'figure/_include/2023/limbang_2023.html', {
		'lbg_2023':lbg_2023,
		'lbg_fd_object':lbg_fd_object,
		'lbg_2023_cumulative':lbg_2023_cumulative,
		'lbg_2023_label':lbg_2023_label,
		'lbg_2023_data':lbg_2023_data,
		})

def limbang_2024_view(request):
	lbg_pf_object = pf_queryset.filter(planting_division__icontains='Limbang')
	lbg_fd_object = fd_queryset.filter(division_name__icontains='Limbang')

	lbg_2024 = lbg_pf_object.filter(year__icontains='2024')
	lbg_2024_cumulative = lbg_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2024_january =lbg_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_february = lbg_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_march = lbg_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_april = lbg_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_may = lbg_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_june = lbg_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_july = lbg_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_august = lbg_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_september = lbg_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_october = lbg_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_november = lbg_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2024_disember = lbg_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lbg_2024_data = [lbg_2024_january, lbg_2024_february, lbg_2024_march, lbg_2024_april,
	lbg_2024_may, lbg_2024_june, lbg_2024_july, lbg_2024_august, lbg_2024_september, 
	lbg_2024_october, lbg_2024_november, lbg_2024_disember]

	return render(request, 'figure/_include/2024/limbang_2024.html', {
		'lbg_2024':lbg_2024,
		'lbg_fd_object':lbg_fd_object,
		'lbg_2024_cumulative':lbg_2024_cumulative,
		'lbg_2024_label':lbg_2024_label,
		'lbg_2024_data':lbg_2024_data,
		})

def limbang_2025_view(request):
	lbg_pf_object = pf_queryset.filter(planting_division__icontains='Limbang')
	lbg_fd_object = fd_queryset.filter(division_name__icontains='Limbang')

	lbg_2025 = lbg_pf_object.filter(year__icontains='2025')
	lbg_2025_cumulative = lbg_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2025_january =lbg_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_february = lbg_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_march = lbg_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_april = lbg_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_may = lbg_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_june = lbg_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_july = lbg_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_august = lbg_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_september = lbg_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_october = lbg_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_november = lbg_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lbg_2025_disember = lbg_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lbg_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lbg_2025_data = [lbg_2025_january, lbg_2025_february, lbg_2025_march, lbg_2025_april,
	lbg_2025_may, lbg_2025_june, lbg_2025_july, lbg_2025_august, lbg_2025_september, 
	lbg_2025_october, lbg_2025_november, lbg_2025_disember]

	return render(request, 'figure/_include/2025/limbang_2025.html', {
		'lbg_2025':lbg_2025,
		'lbg_fd_object':lbg_fd_object,
		'lbg_2025_cumulative':lbg_2025_cumulative,
		'lbg_2025_label':lbg_2025_label,
		'lbg_2025_data':lbg_2025_data,
		})

# LAWAS
def lawas_index_view(request):
	return render(request, 'figure/lawas_index.html')

def lawas_2021_view(request):
	lws_pf_object = pf_queryset.filter(planting_division__icontains='Lawas')
	lws_fd_object = fd_queryset.filter(division_name__icontains='Lawas')

	lws_2021 = lws_pf_object.filter(year__icontains='2021')
	lws_2021_cumulative = lws_2021.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2021_january =lws_2021.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_february = lws_2021.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_march = lws_2021.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_april = lws_2021.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_may = lws_2021.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_june = lws_2021.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_july = lws_2021.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_august = lws_2021.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_september = lws_2021.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_october = lws_2021.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_november = lws_2021.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2021_disember = lws_2021.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2021_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lws_2021_data = [lws_2021_january, lws_2021_february, lws_2021_march, lws_2021_april,
	lws_2021_may, lws_2021_june, lws_2021_july, lws_2021_august, lws_2021_september, 
	lws_2021_october, lws_2021_november, lws_2021_disember]

	return render(request, 'figure/_include/2021/lawas_2021.html', {
		'lws_2021':lws_2021,
		'lws_fd_object':lws_fd_object,
		'lws_2021_cumulative':lws_2021_cumulative,
		'lws_2021_label':lws_2021_label,
		'lws_2021_data':lws_2021_data,
		})

def lawas_2022_view(request):
	lws_pf_object = pf_queryset.filter(planting_division__icontains='Lawas')
	lws_fd_object = fd_queryset.filter(division_name__icontains='Lawas')

	lws_2022 = lws_pf_object.filter(year__icontains='2022')
	lws_2022_cumulative = lws_2022.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2022_january =lws_2022.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_february = lws_2022.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_march = lws_2022.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_april = lws_2022.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_may = lws_2022.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_june = lws_2022.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_july = lws_2022.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_august = lws_2022.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_september = lws_2022.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_october = lws_2022.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_november = lws_2022.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2022_disember = lws_2022.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2022_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lws_2022_data = [lws_2022_january, lws_2022_february, lws_2022_march, lws_2022_april,
	lws_2022_may, lws_2022_june, lws_2022_july, lws_2022_august, lws_2022_september, 
	lws_2022_october, lws_2022_november, lws_2022_disember]

	return render(request, 'figure/_include/2022/lawas_2022.html', {
		'lws_2022':lws_2022,
		'lws_fd_object':lws_fd_object,
		'lws_2022_cumulative':lws_2022_cumulative,
		'lws_2022_label':lws_2022_label,
		'lws_2022_data':lws_2022_data,
		})

def lawas_2023_view(request):
	lws_pf_object = pf_queryset.filter(planting_division__icontains='Lawas')
	lws_fd_object = fd_queryset.filter(division_name__icontains='Lawas')

	lws_2023 = lws_pf_object.filter(year__icontains='2023')
	lws_2023_cumulative = lws_2023.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2023_january =lws_2023.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_february = lws_2023.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_march = lws_2023.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_april = lws_2023.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_may = lws_2023.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_june = lws_2023.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_july = lws_2023.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_august = lws_2023.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_september = lws_2023.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_october = lws_2023.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_november = lws_2023.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2023_disember = lws_2023.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2023_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lws_2023_data = [lws_2023_january, lws_2023_february, lws_2023_march, lws_2023_april,
	lws_2023_may, lws_2023_june, lws_2023_july, lws_2023_august, lws_2023_september, 
	lws_2023_october, lws_2023_november, lws_2023_disember]

	return render(request, 'figure/_include/2023/lawas_2023.html', {
		'lws_2023':lws_2023,
		'lws_fd_object':lws_fd_object,
		'lws_2023_cumulative':lws_2023_cumulative,
		'lws_2023_label':lws_2023_label,
		'lws_2023_data':lws_2023_data,
		})

def lawas_2024_view(request):
	lws_pf_object = pf_queryset.filter(planting_division__icontains='Lawas')
	lws_fd_object = fd_queryset.filter(division_name__icontains='Lawas')

	lws_2024 = lws_pf_object.filter(year__icontains='2024')
	lws_2024_cumulative = lws_2024.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2024_january =lws_2024.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_february = lws_2024.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_march = lws_2024.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_april = lws_2024.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_may = lws_2024.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_june = lws_2024.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_july = lws_2024.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_august = lws_2024.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_september = lws_2024.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_october = lws_2024.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_november = lws_2024.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2024_disember = lws_2024.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2024_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lws_2024_data = [lws_2024_january, lws_2024_february, lws_2024_march, lws_2024_april,
	lws_2024_may, lws_2024_june, lws_2024_july, lws_2024_august, lws_2024_september, 
	lws_2024_october, lws_2024_november, lws_2024_disember]

	return render(request, 'figure/_include/2024/lawas_2024.html', {
		'lws_2024':lws_2024,
		'lws_fd_object':lws_fd_object,
		'lws_2024_cumulative':lws_2024_cumulative,
		'lws_2024_label':lws_2024_label,
		'lws_2024_data':lws_2024_data,
		})

def lawas_2025_view(request):
	lws_pf_object = pf_queryset.filter(planting_division__icontains='Lawas')
	lws_fd_object = fd_queryset.filter(division_name__icontains='Lawas')

	lws_2025 = lws_pf_object.filter(year__icontains='2025')
	lws_2025_cumulative = lws_2025.aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2025_january =lws_2025.filter(month__contains='January').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_february = lws_2025.filter(month__contains='February').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_march = lws_2025.filter(month__contains='March').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_april = lws_2025.filter(month__contains='April').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_may = lws_2025.filter(month__contains='May').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_june = lws_2025.filter(month__contains='June').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_july = lws_2025.filter(month__contains='July').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_august = lws_2025.filter(month__contains='August').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_september = lws_2025.filter(month__contains='September').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_october = lws_2025.filter(month__contains='October').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_november = lws_2025.filter(month__contains='November').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']
	lws_2025_disember = lws_2025.filter(month__contains='Disember').aggregate(Sum('planting_total_trees_planted'))['planting_total_trees_planted__sum']

	lws_2025_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Disember']
	lws_2025_data = [lws_2025_january, lws_2025_february, lws_2025_march, lws_2025_april,
	lws_2025_may, lws_2025_june, lws_2025_july, lws_2025_august, lws_2025_september, 
	lws_2025_october, lws_2025_november, lws_2025_disember]

	return render(request, 'figure/_include/2025/lawas_2025.html', {
		'lws_2025':lws_2025,
		'lws_fd_object':lws_fd_object,
		'lws_2025_cumulative':lws_2025_cumulative,
		'lws_2025_label':lws_2025_label,
		'lws_2025_data':lws_2025_data,
		})

class PlantingFigureDetailView(DetailView):
	model = PlantingFigure
	template_name = 'figure/division_detail.html'