from django.shortcuts import render

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from apps.companies.models import UserCompany
from apps.companies.serializers import UserCompanySerializer


class UserCompanyCreateListAPIView(generics.ListCreateAPIView):
    queryset = UserCompany.objects.filter()
    serializer_class = UserCompanySerializer
    permission_classes = (IsAuthenticated, )


class UserCompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCompany.objects.filter()
    serializer_class = UserCompanySerializer
    permission_classes = (IsAuthenticated,)
