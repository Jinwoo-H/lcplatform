from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name='index'),
	path("discussion/<str:room_name>/", views.room, name="room"),
	path("add_discussion/", views.add_discussion, name='add_discussion')
]