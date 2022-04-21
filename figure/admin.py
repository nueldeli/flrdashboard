from django.contrib import admin
from .models import FigureOverview, FigureByDivision, PlantingFigure

# Register your models here.
class FigureOverviewAdmin(admin.ModelAdmin):
	list_display = ('total_trees_planted', 'total_species', 'total_hectares',)

class FigureByDivisionAdmin(admin.ModelAdmin):
	list_display = ('division_name', 'division_total_trees')

class PlantingFigureAdmin(admin.ModelAdmin):
	list_display = ('planting_program_name', 'planting_division', 'planting_total_trees_planted')

admin.site.site_header = "Dashboard Admin"
admin.site.register(FigureOverview, FigureOverviewAdmin)
admin.site.register(FigureByDivision, FigureByDivisionAdmin)
admin.site.register(PlantingFigure, PlantingFigureAdmin)