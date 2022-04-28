from django.db import models
from django.urls import reverse

# Create your model here
DIVISION_CHOICES = (
		("KUCHING", "Kuching"),
		("SRI AMAN", "Sri Aman"),
		("SARIKEI", "Sarikei"),
		("KAPIT", "Kapit"),
		("SIBU", "Sibu"),
		("BINTULU", "Bintulu"),
		("MIRI", "Miri"),
		("LIMBANG", "Limbang"),
		("LAWAS", "Lawas"),
	)

YEAR_CHOICES = (
		("2025", "2025"),
		("2024", "2024"),
		("2023", "2023"),
		("2022", "2022"),
		("2021", "2021"),
	)

MONTH_CHOICES = (
		("JANUARY", "January"),
		("FEBRUARY", "February"),
		("MARCH", "March"),
		("APRIL", "April"),
		("MAY", "May"),
		("JUNE", "June"),
		("JULY", "July"),
		("AUGUST", "August"),
		("SEPTEMBER", "September"),
		("OCTOBER", "October"),
		("NOVEMBER", "November"),
		("DISEMBER", "Disember")
	)

class FigureOverview(models.Model):
	total_trees_planted = models.IntegerField()
	total_species = models.IntegerField()
	total_hectares = models.FloatField()

	def __str__(self):
		return str(self.total_trees_planted)

	def get_absolute_url(self):
		return reverse('figure_index')

class FigureByDivision(models.Model):
	division_name = models.CharField(max_length=20, choices=DIVISION_CHOICES, default='KUCHING')
	division_total_trees = models.IntegerField()
	division_description = models.TextField(null=True)
	division_img = models.ImageField('Division Image', null=True, upload_to='division_img/')

	class Meta:
		ordering = ['-division_total_trees']

	def __str__(self):
		return self.division_name

	def get_absolute_url(self):
		return reverse('figure_index')

class PlantingFigure(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	day = models.CharField(max_length=5, null=True)
	month = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
	year = models.CharField(max_length=10, choices=YEAR_CHOICES, default='2022')
	planting_program_name = models.CharField(max_length=200)
	planting_division = models.CharField(max_length=20, choices=DIVISION_CHOICES, default='KUCHING')
	planting_total_trees_planted = models.IntegerField()
	planting_species = models.TextField()
	planting_number_of_species = models.IntegerField()
	planting_total_hectares = models.FloatField()
	planting_location = models.CharField(max_length=250)

	class Meta:
		ordering = ['-date_input']

	def __str__(self):
		return self.planting_program_name 

	def get_absolute_url(self):
		return reverse('figure_index')	