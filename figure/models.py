from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class FigureOverview(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	total_trees_planted = models.IntegerField()
	total_species = models.IntegerField()
	total_hectares = models.FloatField()

	def __str__(self):
		return self.total_trees_planted

	def get_absolute_url(self):
		return reverse_lazy('figure_index')

class Division(models.Model):
	division_name = models.CharField(max_length=100)
	division_img = models.ImageField()

	def __str__(self):
		return self.division_name

	def get_absolute_url(self):
		return reverse_lazy('figure_index')

class PlantingFigure(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	date_planted = models.CharField(max_length=50)
	program_name = models.CharField(max_length=200)
	planting_division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
	