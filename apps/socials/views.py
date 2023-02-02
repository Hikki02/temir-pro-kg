from rest_framework import generics

from apps.socials.serializers import UserEmailSerializer, UserSocialSerializer, UserPhoneSerializer, \
    UserBankAccountSerializer, UserBankCartSerializer, UserProductSerializer, UserImageSerializer, UserVideoSerializer, \
    UserQRCodeSerializer, SocialCategorySerializer, MessangerCategorySerializer, UserMessangerSerializer
from apps.socials.models import UserEmail, UserSocial, UserPhone, UserBankAccount, UserBankCart, UserProduct, UserImage, \
    UserVideo, SocialCategory, MessangerCategory, UserMessanger

from rest_framework.permissions import IsAuthenticated

from apps.users.models import User


class UserEmailListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserEmail.objects.filter()
    serializer_class = UserEmailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserEmail.objects.filter(user=self.request.user)


class UserEmailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserEmail.objects.filter()
    serializer_class = UserEmailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserEmail.objects.filter(user=self.request.user)


# - - - - - - - - - - -- - - - - - - USER SOCIAL - - - - - - - - - -
class UserSocialListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserSocial.objects.filter()
    serializer_class = UserSocialSerializer

    def get_queryset(self):
        return UserSocial.objects.filter(user=self.request.user)


class UserSocialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSocial.objects.filter()
    serializer_class = UserSocialSerializer

    def get_queryset(self):
        return UserSocial.objects.filter(user=self.request.user)

# - - - - - - - - - - -- - - - - - - USER Messanger - - - - - - - - - -

class UserMessangerListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserMessanger.objects.filter()
    serializer_class = UserMessangerSerializer

    def get_queryset(self):
        return UserMessanger.objects.filter(user=self.request.user)


class UserMessangerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserMessanger.objects.filter()
    serializer_class = UserMessangerSerializer

    def get_queryset(self):
        return UserMessanger.objects.filter(user=self.request.user)


class UserPhoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserPhone.objects.filter()
    serializer_class = UserPhoneSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserPhone.objects.filter(user=self.request.user)


class UserPhoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPhone.objects.filter()
    serializer_class = UserPhoneSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserPhone.objects.filter(user=self.request.user)


# - - - - - - - - - - - - - - - - -  USER BANK ACCOUNT - - - - - - - - - - - - - - - - -
class UserBankAccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserBankAccount.objects.filter()
    serializer_class = UserBankAccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserBankAccount.objects.filter(user=self.request.user)


class UserBankAccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserBankAccount.objects.filter()
    serializer_class = UserBankAccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserBankAccount.objects.filter(user=self.request.user)


# - - - - - - - - - - - - - - - - -  USER BANK CART - - - - - - - - - - - - - - - - -
class UserBankCartListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserBankCart.objects.filter()
    serializer_class = UserBankCartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserBankCart.objects.filter(user=self.request.user)


class UserBankCartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserBankCart.objects.filter()
    serializer_class = UserBankCartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserBankCart.objects.filter(user=self.request.user)


# - - - - - - - - - - - - - - - - -  USER PRODUCT - - - - - - - - - - - - - - - - -
class UserProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProduct.objects.filter()
    serializer_class = UserProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProduct.objects.filter(user=self.request.user)


class UserProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProduct.objects.filter()
    serializer_class = UserProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProduct.objects.filter(user=self.request.user)


# - - - - - - - - - - - - - - - USER IMAGE - - - - - - - - - - - - - - - - -
class UserImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserImage.objects.filter()
    serializer_class = UserImageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)


class UserImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserImage.objects.filter()
    serializer_class = UserImageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserImage.objects.filter(user=self.request.user)


# - - - - - - - - - - - - - - - USER VIDEO - - - - - - - - - - - - - - - - -
class UserVideoListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserVideo.objects.filter()
    serializer_class = UserVideoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserVideo.objects.filter(user=self.request.user)


class UserVideoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserVideo.objects.filter()
    serializer_class = UserVideoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserVideo.objects.filter(user=self.request.user)


class UserQRCodeRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.filter()
    serializer_class = UserQRCodeSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class SocialCategoryListApiView(generics.ListAPIView):
    queryset = SocialCategory.objects.filter()
    serializer_class = SocialCategorySerializer


class SocialCategoryRetrieveApiView(generics.RetrieveAPIView):
    queryset = SocialCategory.objects.filter()
    serializer_class = SocialCategorySerializer


class MessangerCategoryListApiView(generics.ListAPIView):
    queryset = MessangerCategory.objects.filter()
    serializer_class = MessangerCategorySerializer


class MessangerCategoryRetrieveApiView(generics.RetrieveAPIView):
    queryset = MessangerCategory.objects.filter()
    serializer_class = MessangerCategorySerializer
