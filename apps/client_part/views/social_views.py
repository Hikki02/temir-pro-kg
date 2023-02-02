from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.client_part.filters import UserProductFilter, UserEmailFilter, UserSocialFilter, UserMessangerFilter, \
    UserPhoneFilter, UserBankAccountFilter, UserBankCartFilter, UserImageFilter, UserVideoFilter
from apps.socials.serializers import UserEmailSerializer, UserSocialSerializer, UserPhoneSerializer, \
    UserBankAccountSerializer, UserBankCartSerializer, UserProductSerializer, UserImageSerializer, UserVideoSerializer, \
    UserQRCodeSerializer, UserMessangerSerializer
from apps.socials.models import UserEmail, UserSocial, UserPhone, UserBankAccount, UserBankCart, UserProduct, UserImage, \
    UserVideo, UserMessanger
from apps.users.models import User


class UserEmailListAPIView(generics.ListAPIView):
    queryset = UserEmail.objects.filter()
    serializer_class = UserEmailSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserEmailFilter


class UserEmailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserEmail.objects.filter()
    serializer_class = UserEmailSerializer


class UserSocialListAPIView(generics.ListAPIView):
    queryset = UserSocial.objects.filter()
    serializer_class = UserSocialSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserSocialFilter


class UserSocialRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserSocial.objects.filter()
    serializer_class = UserSocialSerializer


class UserMessangerListAPIView(generics.ListAPIView):
    queryset = UserMessanger.objects.filter()
    serializer_class = UserMessangerSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserMessangerFilter


class UserMessangerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserMessanger.objects.filter()
    serializer_class = UserMessangerSerializer


class UserPhoneListAPIView(generics.ListAPIView):
    queryset = UserPhone.objects.filter()
    serializer_class = UserPhoneSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserPhoneFilter


class UserPhoneRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserPhone.objects.filter()
    serializer_class = UserPhoneSerializer


# - - - - - - - - - - - - - - - - -  USER BANK ACCOUNT - - - - - - - - - - - - - - - - -
class UserBankAccountListAPIView(generics.ListAPIView):
    queryset = UserBankAccount.objects.filter()
    serializer_class = UserBankAccountSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserBankAccountFilter


class UserBankAccountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserBankAccount.objects.filter()
    serializer_class = UserBankAccountSerializer


# - - - - - - - - - - - - - - - - -  USER BANK CART - - - - - - - - - - - - - - - - -
class UserBankCartListAPIView(generics.ListAPIView):
    queryset = UserBankCart.objects.filter()
    serializer_class = UserBankCartSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserBankCartFilter


class UserBankCartRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserBankCart.objects.filter()
    serializer_class = UserBankCartSerializer


# - - - - - - - - - - - - - - - - -  USER aPRODUCT - - - - - - - - - - - - - - - - -
class UserProductListAPIView(generics.ListAPIView):
    queryset = UserProduct.objects.filter()
    serializer_class = UserProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserProductFilter


class UserProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserProduct.objects.filter()
    serializer_class = UserProductSerializer


# - - - - - - - - - - - - - - - USER IMAGE - - - - - - - - - - - - - - - - -
class UserImageListAPIView(generics.ListAPIView):
    queryset = UserImage.objects.filter()
    serializer_class = UserImageSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserImageFilter


class UserImageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserImage.objects.filter()
    serializer_class = UserImageSerializer


# - - - - - - - - - - - - - - - USER VIDEO - - - - - - - - - - - - - - - - -
class UserVideoListAPIView(generics.ListAPIView):
    queryset = UserVideo.objects.filter()
    serializer_class = UserVideoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['user', ]
    filterset_class = UserVideoFilter


class UserVideoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserVideo.objects.filter()
    serializer_class = UserVideoSerializer


class UserQRCodeRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.filter()
    serializer_class = UserQRCodeSerializer
