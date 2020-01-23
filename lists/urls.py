from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_list2, name='new_list'),
    path('<list_id>/', views.view_list, name='view_list'),
    path('users/<email>/', views.my_lists, name='my_lists'),
]