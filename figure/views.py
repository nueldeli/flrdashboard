from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class FigureIndexView(TemplateView):
	template_name = 'figure/figure_index.html'