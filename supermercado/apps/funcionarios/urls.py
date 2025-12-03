from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Home = login
    path('logout/', views.logout_view, name='logout'),
    path('listar/', views.employee_list, name='employee_list'),
    path('novo/', views.employee_create, name='employee_create'),
    path('editar/<int:pk>/', views.employee_update, name='employee_update'),
    path('deletar/<int:pk>/', views.employee_delete, name='employee_delete'),
]
