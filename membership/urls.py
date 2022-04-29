from django.urls import path
from .views import SignUpView, user_profile_view

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('user_profile/', user_profile_view, name='user_profile')
]