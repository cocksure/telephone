from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_departments, name='list_departments'),
    path('my-table/', views.my_table_view, name='my_table_view'),
]
