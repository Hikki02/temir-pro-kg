from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.orders.models import OrderItem, Order
from apps.orders.serializers import CartItemSerializer, CartItemAddSerializer
from apps.products.models import Product


# Create your views here.


class OrderItemView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter()


class OrderItmeRetrieve(generics.RetrieveAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter()


class OrderItemPostView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request):
        request_body = request.data
        srz = CartItemSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST, )

    @classmethod
    def get_extra_actions(cls):
        return []


class OrderItemAddView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = CartItemAddSerializer

    # def perform_create(self, serializer):
    #     self.serializer.save()


class OrderItemDelView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()

    def delete(self, request, pk, format=None):
        user = request.applicant
        cart_item = OrderItem.objects.filter(user=user)
        target_product = get_object_or_404(cart_item, pk=pk)
        product = get_object_or_404(Product, id=target_product.product.id)
        product.save()
        target_product.delete()
        return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})


class OrderItemAddOneView(APIView):

    def get(self, request, pk, format=None):
        user = request.applicanter
        cart_item = OrderItem.objects.filter(user=user)
        target_product = cart_item.get(pk=pk)
        product = get_object_or_404(Product, id=target_product.product.id)


class OrderItemReduceOneView(APIView):

    def get(self, request, pk, format=None):
        user = request.applicant
        cart_item = OrderItem.objects.filter(user=user)
        target_product = cart_item.get(pk=pk)
        product = get_object_or_404(Product, id=target_product.product.id)
