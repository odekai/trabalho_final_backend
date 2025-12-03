from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('nova/', views.sale_create, name='sale_create'),
    path('itens/<int:venda_id>/', views.sale_add_item, name='sale_add_item'),
]
