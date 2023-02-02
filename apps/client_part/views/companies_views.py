from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.client_part.filters import UserCompanyFilter
from apps.companies.models import UserCompany
from apps.companies.serializers import UserCompanySerializer


class UserCompanyListAPIView(generics.ListAPIView):
    queryset = UserCompany.objects.filter()
    serializer_class = UserCompanySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserCompanyFilter


class UserCompanyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserCompany.objects.filter()
    serializer_class = UserCompanySerializer
