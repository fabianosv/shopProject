from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_form, name='cliente_create'),
    path('clientes/<int:id>/', views.cliente_form, name='cliente_update'),
    # Similar paths for `produtos` and `vendas`
    path ('produtos/', views.produto_list, name='produto_list'),
    path ('productos/novo/', views.produto_form, name='produto_create'),
    path('produtos/<int:id>/', views.produto_form, name='produto_update'),

    path ('vendas/', views.produto_list, name='venda_list'),
    path ('vendas/novo/', views.produto_form, name='venda_create'),
    path('vendas/<int:id>/', views.produto_form, name='venda_update'),


]