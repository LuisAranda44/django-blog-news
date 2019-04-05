from django.urls import path


from . import views

urlpatterns = [
    path('',views.NewList.as_view(), name = 'new'),
    path('v1', views.new_list, name='new_list'),
    path('v1/news/<int:pk>/', views.new_detail, name='new_detail'),
    path('v1/news/create',views.new_add, name="new_add"),
    path('v1/news/<int:pk>/edit/', views.new_edit, name='new_edit'),
    path('v1/news/<int:pk>/delete/', views.new_delete, name='new_delete'),
    path('v2',views.NewList.as_view(), name = "new_list_class"),
    path('v2/news/<int:pk>/', views.NewDetail.as_view(), name='new_detail_class'),
    path('v2/news/create/',views.NewCreate.as_view(), name="new_add_class"),
    path('v2/news/<int:pk>/edit/', views.NewUpdate.as_view(), name="new_edit_class"),
    path('v2/news/<int:pk>/delete/', views.NewDelete.as_view(), name='new_delete_class'),
]