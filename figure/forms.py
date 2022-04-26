from django import forms
from .models import FigureOverview, FigureByDivision, PlantingFigure

class UpdateFigureOverviewForm(forms.ModelForm):
	class Meta:
		model = FigureOverview
		fields = ('total_trees_planted', 'total_species', 'total_hectares')

		widgets = {
			'total_trees_planted':forms.NumberInput(attrs={'class':'form-control'}),
			'total_species':forms.NumberInput(attrs={'class':'form-control'}),
			'total_hectares':forms.NumberInput(attrs={'class':'form-control'}),
		}

class UpdateKuchingDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

#class AddPlantingFigureForm(forms.ModelForm):
	#class Meta:
		#model = PlantingFigure
		#fields = ('date_planted', 'planting_program_name', 'planting_division', 'planting_total_trees_planted', 'planting_species', 'planting_number_of_species', 'planting_total_hectares', 'planting_location')

		#widgets = {
			#'date_planted':forms.TextInput(attrs={'class':'form-control'}),
			#'planting_program_name':forms.TextInput(attrs={'class':'form-control'}),
			#'planting_division':forms.TextInput(),
			#'planting_total_trees_planted':forms.NumberInput(attrs={'class':'form-control'}),
			#'planting_species':forms.Textarea(attrs={'class':'form-control'}),
			#'planting_number_of_species':forms.NumberInput(attrs={'class':'form-control'}),
			#'planting_total_hectares':forms.FloatField(),
			#'planting_location':forms.TextInput(attrs={'class':'form-control'})
		#}

#class UpdatePlantingFigureForm(forms.ModelForm):
	#class Meta:
		#model = PlantingFigure
		#fields = ('date_planted', 'planting_program_name', 'planting_division', 'planting_total_trees_planted', 'planting_species', 'planting_number_of_species', 'planting_total_hectares', 'planting_location')

		#widgets = {
			#'date_planted':forms.TextInput(attrs={'class':'form-control'}),
			#'planting_program_name':forms.TextInput(attrs={'class':'form-control'}),
			#'planting_division':forms.TextInput(),
			#'planting_total_trees_planted':forms.NumberInput(attrs={'class':'form-control'}),
			#'planting_species':forms.Textarea(attrs={'class':'form-control'}),
			#'planting_number_of_species':forms.NumberInput(attrs={'class':'form-control'}),
			#'planting_total_hectares':forms.FloatField(),
			#'planting_location':forms.TextInput(attrs={'class':'form-control'})
		#}
