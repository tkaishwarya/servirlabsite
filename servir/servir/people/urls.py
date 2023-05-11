from django.urls import path
from .views import (
	people_create_view,
	people_list_view,
	people_detail_view,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('', views.index, name='index'),
	path('api/create/', people_create_view),
	path('api/list/', people_list_view),
	path('api/<int:person_id>/', people_detail_view),
]
urlpatterns += staticfiles_urlpatterns()
