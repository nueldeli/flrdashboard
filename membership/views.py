from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
	template_name = 'registration/signup.html'
	form_class = SignUpForm
	success_url = reverse_lazy('login')

def user_profile_view(request):
	return render(request, 'registration/user_profile.html')

