from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_list, name='new_list'),
    path('new/<int:pk>/', views.new_detail, name='new_detail'),
]