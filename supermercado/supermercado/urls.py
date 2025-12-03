from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('produtos/', include('apps.produtos.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('entregas/', include('apps.entregas.urls')),
    path('vendas/', include('apps.vendas.urls')),

    path('', include('apps.funcionarios.urls')),  # Home e Login
]
