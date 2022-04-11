from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class FigureOverview(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	total_trees_planted = models.IntegerField()
	total_species = models.IntegerField()
	total_hectares = models.FloatField()

	def __str__(self):
		return str(self.total_trees_planted)

	def get_absolute_url(self):
		return reverse_lazy('figure_index')

class Division(models.Model):
	division_name = models.CharField(max_length=100)
	division_img = models.ImageField('Division', null=True, upload_to='division_img/')

	def __str__(self):
		return self.division_name

	def get_absolute_url(self):
		return reverse_lazy('figure_index')

class PlantingFigure(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	date_planted = models.CharField(max_length=50)
	planting_program_name = models.CharField(max_length=200)
	planting_division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
	planting_total_trees_planted = models.IntegerField()
	planting_species = models.TextField()
	planting_number_of_species = models.IntegerField()
	planting_total_hectares = models.FloatField()
	planting_location = models.CharField(max_length=250)

	class Meta:
		ordering = ['-planting_total_trees_planted']

	def __str__(self):
		return self.planting_program_name

	def get_absolute_url(self):
		return reverse_lazy('figure_index')

class FigureByDivision(models.Model):
	figure_division = models.ForeignKey(Division, null=True, on_delete=models.CASCADE)
	division_total_trees_planted = models.IntegerField()

	def __str__(self):
		return self.figure_division + ' ' + str(self.division_total_trees_planted)

	def get_absolute_url(self):
		return reverse_lazy('figure_index')
