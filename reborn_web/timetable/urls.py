from django.conf import settings
from django.urls import path
from . import views


app_name = 'timetable'

urlpatterns = [
    path('', views.time_table_view, name='timetable_list'),
    path('update/', views.time_table_update_view, name='timetable_update'),
]