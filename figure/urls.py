from django.urls import path
from .views import (figure_index_view, 
kuching_index_view, kuching_2021_view, kuching_2022_view, kuching_2023_view, kuching_2024_view, kuching_2025_view,
sri_aman_index_view, sri_aman_2021_view, sri_aman_2022_view, sri_aman_2023_view, sri_aman_2024_view, sri_aman_2025_view,
sarikei_index_view, sarikei_2021_view, sarikei_2022_view, sarikei_2023_view, sarikei_2024_view, sarikei_2025_view,
kapit_index_view, kapit_2021_view, kapit_2022_view, kapit_2023_view, kapit_2024_view, kapit_2025_view,
sibu_index_view, sibu_2021_view, sibu_2022_view, sibu_2023_view, sibu_2024_view, sibu_2025_view,
bintulu_index_view, bintulu_2021_view, bintulu_2022_view, bintulu_2023_view, bintulu_2024_view, bintulu_2025_view,
miri_index_view, miri_2021_view, miri_2022_view, miri_2023_view, miri_2024_view, miri_2025_view,
limbang_index_view, limbang_2021_view, limbang_2022_view, limbang_2023_view, limbang_2024_view, limbang_2025_view,
lawas_index_view, lawas_2021_view, lawas_2022_view, lawas_2023_view, lawas_2024_view, lawas_2025_view,
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
	path('sarikei_2024/', sarikei_2024_view, name='sarikei_2024'),
	path('sarikei_2025/', sarikei_2025_view, name='sarikei_2025'),
	path('kapit_index/', kapit_index_view, name='kapit_index'),
	path('kapit_2021/', kapit_2021_view, name='kapit_2021'),
	path('kapit_2022/', kapit_2022_view, name='kapit_2022'),
	path('kapit_2023/', kapit_2023_view, name='kapit_2023'),
	path('kapit_2024/', kapit_2024_view, name='kapit_2024'),
	path('kapit_2025/', kapit_2025_view, name='kapit_2025'),
	path('sibu_index/', sibu_index_view, name='sibu_index'),
	path('sibu_2021/', sibu_2021_view, name='sibu_2021'),
	path('sibu_2022/', sibu_2022_view, name='sibu_2022'),
	path('sibu_2023/', sibu_2023_view, name='sibu_2023'),
	path('sibu_2024/', sibu_2024_view, name='sibu_2024'),
	path('sibu_2025/', sibu_2025_view, name='sibu_2025'),
	path('bintulu_index/', bintulu_index_view, name='bintulu_index'),
	path('bintulu_2021/', bintulu_2021_view, name='bintulu_2021'),
	path('bintulu_2022/', bintulu_2022_view, name='bintulu_2022'),
	path('bintulu_2023/', bintulu_2023_view, name='bintulu_2023'),
	path('bintulu_2024/', bintulu_2024_view, name='bintulu_2024'),
	path('bintulu_2025/', bintulu_2025_view, name='bintulu_2025'),
	path('miri_index/', miri_index_view, name='miri_index'),
	path('miri_2021/', miri_2021_view, name='miri_2021'),
	path('miri_2022/', miri_2022_view, name='miri_2022'),
	path('miri_2023/', miri_2023_view, name='miri_2023'),
	path('miri_2024/', miri_2024_view, name='miri_2024'),
	path('miri_2025/', miri_2025_view, name='miri_2025'),
	path('limbang_index/', limbang_index_view, name='limbang_index'),
	path('limbang_2021/', limbang_2021_view, name='limbang_2021'),
	path('limbang_2022/', limbang_2022_view, name='limbang_2022'),
	path('limbang_2023/', limbang_2023_view, name='limbang_2023'),
	path('limbang_2024/', limbang_2024_view, name='limbang_2024'),
	path('limbang_2025/', limbang_2025_view, name='limbang_2025'),
	path('lawas_index/', lawas_index_view, name='lawas_index'),
	path('lawas_2021/', lawas_2021_view, name='lawas_2021'),
	path('lawas_2022/', lawas_2022_view, name='lawas_2022'),
	path('lawas_2023/', lawas_2023_view, name='lawas_2023'),
	path('lawas_2024/', lawas_2024_view, name='lawas_2024'),
	path('lawas_2025/', lawas_2025_view, name='lawas_2025'),
	path('planting_detail/<int:pk>', PlantingFigureDetailView.as_view(), name='division_detail')
]