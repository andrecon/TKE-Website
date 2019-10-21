from django.urls import path, include
from . import views
from . import philan

from django.contrib.auth import views as auth_views



urlpatterns = [
		path('', views.GalleryView.as_view(), name='index'),
		#path('philanthropy/', philan.index),
		path('philanthropy/', philan.EventView.as_view(), name='philanthropy'),
		path('post/', philan.CreateEventView.as_view()),
		path('photoPost/',views.CreateImageView.as_view()),
		# path('signup/', views.SignUp.as_view(), name='signup'),
		path('signup/', views.signup, name='signup'),
		path('login/', auth_views.LoginView.as_view(), name='login'),
    	path('logout/', views.logout_view, name='logout'),
]