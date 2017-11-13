from django.conf.urls import url
from . import views

app_name = 'extropy'
	
urlpatterns = [
	# extropy/
	url(r'^$', views.index, name="index"),
]