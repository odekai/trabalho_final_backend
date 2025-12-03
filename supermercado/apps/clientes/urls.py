from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('novo/', views.client_create, name='client_create'),
    path('editar/<int:pk>/', views.client_update, name='client_update'),
    path('deletar/<int:pk>/', views.client_delete, name='client_delete'),
]
