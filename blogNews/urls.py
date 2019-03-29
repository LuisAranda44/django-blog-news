from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_list, name='new_list'),
]