from rest_framework import viewsets, generics
from .models import Product, Category, PreProduct
from .serializers import ProductSerializer, ModelSerializer, PreProductSerializer
from rest_framework import filters

# Create your views here.


class ModelView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductView(viewsets.ModelViewSet):
    queryset = Product.available.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class PreProductView(viewsets.ModelViewSet):
    queryset = PreProduct.objects.all()
    serializer_class = PreProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company_name']






class PreProductView(viewsets.ModelViewSet):
    queryset = PreProduct.objects.all()
    serializer_class = PreProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company_name']





