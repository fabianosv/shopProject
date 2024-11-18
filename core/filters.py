import django_filters
from .models import Cliente, Produto, Venda


class ClienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')  # Busca parcial por nome
    email = django_filters.CharFilter(lookup_expr='icontains')  # Busca parcial por email
    telefone = django_filters.CharFilter(lookup_expr='icontains')  # Busca parcial por telefone

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']


class ProdutoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')  # Busca parcial por nome
    preco_min = django_filters.NumberFilter(field_name='preco', lookup_expr='gte')  # Preço mínimo
    preco_max = django_filters.NumberFilter(field_name='preco', lookup_expr='lte')  # Preço máximo
    quantidade_estoque_min = django_filters.NumberFilter(field_name='quantidade_estoque', lookup_expr='gte')  # Estoque mínimo

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'quantidade_estoque']


class VendaFilter(django_filters.FilterSet):
    cliente_nome = django_filters.CharFilter(field_name='cliente__nome', lookup_expr='icontains')  # Nome do cliente
    produto_nome = django_filters.CharFilter(field_name='produto__nome', lookup_expr='icontains')  # Nome do produto
    data_min = django_filters.DateFilter(field_name='data_venda', lookup_expr='gte')  # Data mínima
    data_max = django_filters.DateFilter(field_name='data_venda', lookup_expr='lte')  # Data máxima

    class Meta:
        model = Venda
        fields = ['cliente', 'produto', 'data_venda']