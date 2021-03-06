from django.urls import path, include
from . import views
from . import philan
from . import volunteer
from . import about
from . import account

from django.contrib.auth import views as auth_views



urlpatterns = [
		path('', views.GalleryView.as_view(), name='index'),

		path('philanthropy/', philan.EventView.as_view(), name='philanthropy'),
		# path('philanthropy/', philan.index, name='philanthropy'),
		

		path('postdata/', philan.posts_view),
		path('post/', philan.CreateEventView.as_view()),

		# path('account/', account.index),
		path('account/', account.EventView.as_view(), name='account'),

		path('volunteer/', volunteer.CreateVolunteerView.as_view()),
		


		path('photoPost/',views.CreateImageView.as_view()),
		# path('signup/', views.SignUp.as_view(), name='signup'),
		path('signup/', views.signup, name='signup'),
		path('login/', auth_views.LoginView.as_view(), name='login'),
    	path('logout/', views.logout_view, name='logout'),
		path('contact/', views.contact, name='contact'),
		path('aboutUs/', about.index, name="about"),
		path('chat/', views.chat, name="chat"),
        path('chat/<str:room_name>/', views.room, name='room'),
		path('rush/', views.rush, name='rush'),
		path('thanks/', views.thanks, name='thanks'),
]