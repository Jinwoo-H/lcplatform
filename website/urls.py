from django.urls import path
from . import views


urlpatterns = [	
	path('', views.home, name='home'),
	path('logout/', views.logout_user, name='logout'),
	path('details/<int:pk>', views.details, name='details'),
	path('add_question/', views.add_question, name='add_question'),
	path('register/', views.register_user, name='register'),
	path('update_question/<int:pk>', views.update_question, name='update_question'),
	path('remove_question/<int:pk>', views.remove_question, name='remove_question')
]