from django.contrib import admin
from .models import FigureOverview, Division, PlantingFigure, FigureByDivision

# Register your models here.
class FigureOverviewAdmin(admin.ModelAdmin):
	list_display = ('total_trees_planted', 'total_species', 'total_hectares',)

class DivisionAdmin(admin.ModelAdmin):
	list_display = ('division_name',)

class PlantingFigureAdmin(admin.ModelAdmin):
	list_display = ('planting_program_name', 'planting_division',)

class FigureByDivisionAdmin(admin.ModelAdmin):
	list_display = ('figure_division', 'figure_division_total')

admin.site.site_header = "Dashboard Admin"
admin.site.register(FigureOverview, FigureOverviewAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(PlantingFigure, PlantingFigureAdmin)
admin.site.register(FigureByDivision, FigureByDivisionAdmin)