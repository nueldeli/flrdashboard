from django import forms
from .models import FigureOverview, FigureByDivision, PlantingFigure
from django.utils.translation import gettext_lazy as _

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

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateSriAmanDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateSarikeiDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateKapitDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateSibuDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateBintuluDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateMiriDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateLimbangDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class UpdateLawasDivisionForm(forms.ModelForm):
	class Meta:
		model = FigureByDivision
		fields = ('division_name', 'division_total_trees', 'division_img', 'division_description')

		widgets = {
			'division_name':forms.TextInput(attrs={'class':'form-control'}),
			'division_total_trees':forms.NumberInput(attrs={'class':'form-control'}),
			'division_img':forms.FileInput(),
			'division_description':forms.Textarea(attrs={'class':'form-control'})
		}

		labels= {
			'division_total_trees':_('Total trees'),
			'division_img':_('Division Image'),
			'division_description':_('Remarks')
		}

class AddPlantingFigureForm(forms.ModelForm):
	class Meta:
		model = PlantingFigure
		fields = ('day', 'month', 'year', 'planting_program_name', 'planting_division', 'planting_total_trees_planted', 'planting_species', 'planting_number_of_species', 'planting_total_hectares', 'planting_location')

		widgets = {
			'day': forms.TextInput(attrs={'class':'form-control'}),
			'month':forms.Select(attrs={'class':'form-control'}),
			'year':forms.Select(attrs={'class':'form-control'}),
			'planting_program_name':forms.TextInput(attrs={'class':'form-control'}),
			'planting_division':forms.Select(attrs={'class':'form-control'}),
			'planting_total_trees_planted':forms.NumberInput(attrs={'class':'form-control'}),
			'planting_species':forms.Textarea(attrs={'class':'form-control'}),
			'planting_number_of_species':forms.NumberInput(attrs={'class':'form-control'}),
			'planting_total_hectares':forms.NumberInput(attrs={'class':'form-control'}),
			'planting_location':forms.TextInput(attrs={'class':'form-control'})
		}

		labels = {
			'planting_program_name':_('Program name'),
			'planting_division':_('Division'),
			'planting_total_trees_planted':_('Total trees'),
			'planting_species':_('Species'),
			'planting_number_of_species':_('Number of species'),
			'planting_total_hectares':_('Total hectares'),
			'planting_location':_('Location')
		}

class UpdatePlantingFigureForm(forms.ModelForm):
	class Meta:
		model = PlantingFigure
		fields = ('day', 'month', 'year', 'planting_program_name', 'planting_division', 'planting_total_trees_planted', 'planting_species', 'planting_number_of_species', 'planting_total_hectares', 'planting_location')

		widgets = {
			'day': forms.TextInput(attrs={'class':'form-control'}),
			'month':forms.Select(attrs={'class':'form-control'}),
			'year':forms.Select(attrs={'class':'form-control'}),
			'planting_program_name':forms.TextInput(attrs={'class':'form-control'}),
			'planting_division':forms.Select(attrs={'class':'form-control'}),
			'planting_total_trees_planted':forms.NumberInput(attrs={'class':'form-control'}),
			'planting_species':forms.Textarea(attrs={'class':'form-control'}),
			'planting_number_of_species':forms.NumberInput(attrs={'class':'form-control'}),
			'planting_total_hectares':forms.NumberInput(attrs={'class':'form-control'}),
			'planting_location':forms.TextInput(attrs={'class':'form-control'})
		}

		labels = {
			'planting_program_name':_('Program name'),
			'planting_division':_('Division'),
			'planting_total_trees_planted':_('Total trees'),
			'planting_species':_('Species'),
			'planting_number_of_species':_('Number of species'),
			'planting_total_hectares':_('Total hectares'),
			'planting_location':_('Location')
		}
