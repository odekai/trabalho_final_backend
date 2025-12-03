from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_list, name='delivery_list'),
    path('nova/', views.delivery_create, name='delivery_create'),
]
