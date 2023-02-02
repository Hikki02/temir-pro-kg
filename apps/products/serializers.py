from rest_framework import serializers
from .models import Product, Category, PreProduct


class ModelSerializer(serializers.ModelSerializer):

    """
    serializer for model that serialize:
    ('id', 'name')
    and add relation to category serializer \nbased model
    """

    class Meta:
        model = Category
        fields = (
            'id', 'uuid', 'title',
        )


class ProductSerializer(serializers.ModelSerializer):
    """
    serializer for products that serialize:
    ('id', "name", "price", 'type_of_product', 'kind_of_product'
            "is_available", "quantity", "image", 'description')
    and add relation to category serializer \nbased on Product model

    """

    class Meta:
        model = Product
        fields = (
            'id', 'uuid', "name", "price",
            "is_available", "quantity", "image", 'description'
        )


class PreProductSerializer(serializers.ModelSerializer):
    """
    serializer for pre-product that serialize:
    ('id', 'product', 'quantity', 'name_company', 'logo')
    """
    class Meta:
        model = PreProduct
        fields = (
            'id', 'uuid', 'product', 'name_company', 'logo'
        )



