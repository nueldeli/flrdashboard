from django.contrib import admin
from .models import FigureOverview, Division, PlantingFigure

# Register your models here.
class FigureOverviewAdmin(admin.ModelAdmin):
	list_display = ('total_trees_planted', 'total_species', 'total_hectares')

class DivisionAdmin(admin.ModelAdmin):
	list_display = ('division_name')

class PlantingFigureAdmin(admin.ModelAdmin):
	list_display = ('planting_program_name', 'planting_division')

admin.site.register(FigureOverview, FigureOverviewAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(PlantingFigure, PlantingFigureAdmin)