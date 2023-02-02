from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.applications.models import Checkout, ContactUs
from apps.applications.serializers import ContactUsSerializer, CheckoutSerializer
# Create your views here.


class PostCheckoutAPIView(generics.UpdateAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'created_at']
    serializer_class = CheckoutSerializer
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['created_at', 'in_archive']
    queryset = Checkout.objects.all()
    # lookup_field = 'id'


    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #
    #     if serializer.is_valid():
    #         # serializer.update(instance, checkout = )
    #         instance.save()
    #         return Response({"message": "Done"})
    #
    #     else:
    #         return Response({"message": "failed", "details": serializer.errors})
    #

    # @classmethod
    # def get_extra_actions(cls):
    #     return []


class GetCheckoutAPIView(APIView):

    def get(self, request, pk):
        try:
            product = Checkout.objects.get(id=pk)
        except Checkout.DoesNotExist:
            return Response({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = CheckoutSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)


class PostContactUsAPIView(generics.ListCreateAPIView):

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['full_name', 'created_at']
    serializer_class = ContactUsSerializer
    search_fields = ['full_name', ]
    ordering_fields = ['created_at', 'in_archive']
    queryset = ContactUs.objects.all()

    def post(self, request):
        request_body = request.data
        srz = ContactUsSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST, )


class GetContactUsAPIView(APIView):

    def get(self, request, pk):
        try:
            product = ContactUs.objects.get(id=pk)
        except ContactUs.DoesNotExist:
            return Response({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = ContactUsSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)
