from rest_framework import serializers
from django.shortcuts import get_object_or_404

from apps.orders.models import OrderItem, Order
from apps.applications.models import Checkout
from apps.products.models import Product


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id', 'uuid'
        )



class CartItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id', 'order', 'product', 'quantity'
        )

    # def create(self, validated_data):
    #     products = validated_data.get('products')
    #     order = Order.objects.create(
    #         uuid=validated_data.get('uuid')
    #     )
    #     for p in products:
    #         product = Product.objects.filter(id=p['prod_id']).first()
    #         OrderItem.objects.create(
    #             order=order,
    #             product=product,
    #             quantity=p['quantity']
    #         )
    #     order_items = order.orderitem_set.all()
    #     Checkout.objects.create(order_id=order, amount=sum([i.sum_price for i in order_items]) if order_items else 0)
    #
    #     return order


    # def create(self, validated_data):
    #     try:
    #         user = Checkout.objects.get(id=self.context['request'].user.id)
    #     except Checkout.DoesNotExist:
    #         user = 'Не существует Checkout'
    #     try:
    #         product = get_object_or_404(Product, id=self.validated_data['uuid'])
    #     except Product.DoesNotExist:
    #         product = 'Не существует Product'
    #     user = get_object_or_404(Checkout, uuid=self.context['request'].user.id)
    #     product = get_object_or_404(Product, uuid=validated_data['uuid'])
    #
    #     cart_item = OrderItem.objects.create(
    #         product=product,
    #         user=user,
    #         )
    #     cart_item.save()
    #     cart_item.add_amount()
    #     product.save()
    #     return cart_item
