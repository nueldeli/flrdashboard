from django import forms
from .models import FigureOverview, FigureByDivision

class UpdateFigureOverviewForm(forms.ModelForm):
	class Meta:
		model = FigureOverview
		fields = ('total_trees_planted', 'total_species', 'total_hectares')

		widgets = {
			'total_trees_planted':forms.NumberInput(attrs={'class':'form-control'}),
			'total_species':forms.NumberInput(attrs={'class':'form-control'}),
			'total_hectares':forms.NumberInput(attrs={'class':'form-control'}),
		}

class UpdateFigureByDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('figure_division', 'figure_division_total')

		widgets = {
			'figure_division':forms.TextInput(attrs={'class':'form-control'}),
			'figure_division_total':forms.NumberInput(attrs={'class':'form-control'})
		}