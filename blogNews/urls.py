from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.new_list, name='new_list'),
    path('v1/news/<int:pk>/', views.new_detail, name='new_detail'),
    path('v1/news/create',views.new_add, name="new_add"),
    path('v1/news/<int:pk>/edit/', views.new_edit, name='new_edit'),
]