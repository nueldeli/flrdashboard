from django.urls import path
from .views import (figure_index_view, 
kuching_index_view, kuching_2021_view, kuching_2022_view, kuching_2023_view, kuching_2024_view, kuching_2025_view,
sri_aman_index_view, sri_aman_2021_view, sri_aman_2022_view, sri_aman_2023_view, sri_aman_2024_view, sri_aman_2025_view,
sarikei_index_view, sarikei_2021_view, sarikei_2022_view, sarikei_2023_view,
PlantingFigureDetailView)

urlpatterns = [
	path('', figure_index_view, name='figure_index'),
	path('kuching_index/', kuching_index_view, name='kuching_index'),
	path('kuching_2021/', kuching_2021_view, name='kuching_2021'),
	path('kuching_2022/', kuching_2022_view, name='kuching_2022'),
	path('kuching_2023/', kuching_2023_view, name='kuching_2023'),
	path('kuching_2024/', kuching_2024_view, name='kuching_2024'),
	path('kuching_2025/', kuching_2025_view, name='kuching_2025'),
	path('sri_aman_index/', sri_aman_index_view, name='sri_aman_index'),
	path('sri_aman_2021/', sri_aman_2021_view, name='sri_aman_2021'),
	path('sri_aman_2022/', sri_aman_2022_view, name='sri_aman_2022'),
	path('sri_aman_2023/', sri_aman_2023_view, name='sri_aman_2023'),
	path('sri_aman_2024/', sri_aman_2024_view, name='sri_aman_2024'),
	path('sri_aman_2025/', sri_aman_2025_view, name='sri_aman_2025'),
	path('sarikei_index/', sarikei_index_view, name='sarikei_index'),
	path('sarikei_2021/', sarikei_2021_view, name='sarikei_2021'),
	path('sarikei_2022/', sarikei_2022_view, name='sarikei_2022'),
	path('sarikei_2023/', sarikei_2023_view, name='sarikei_2023'),
	path('planting_detail/<int:pk>', PlantingFigureDetailView.as_view(), name='division_detail')
]