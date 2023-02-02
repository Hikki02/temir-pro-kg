from rest_framework import serializers

from .base import BaseSocialSerializer
from .models import UserEmail, UserSocial, UserPhone, UserBankAccount, UserProduct, UserImage, UserVideo, \
    SocialCategory, UserMessanger, UserBankCart

# - - - - - - - - - - - - - - - USER EMAIL - - - - - - - - - - - - - - - - -
from ..users.models import User


class UserEmailSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = UserEmail
        fields = BaseSocialSerializer.Meta.fields + ['email']


# - - - - - - - - - - - - - - - USER SOCIAL - - - - - - - - - - - - - - - - -

class SocialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialCategory
        fields = ('id', 'name')


class MessangerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialCategory
        fields = ('id', 'name')


class UserSocialSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    url = serializers.URLField()

    class Meta:
        model = UserSocial
        fields = BaseSocialSerializer.Meta.fields + ['url', 'social']


class UserMessangerSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    url = serializers.URLField()

    class Meta:
        model = UserMessanger
        fields = BaseSocialSerializer.Meta.fields + ['url', 'messanger']


# - - - - - - - - - - - - - - - USER PHONE - - - - - - - - - - - - - - - - -
class UserPhoneSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    phone_number = serializers.CharField()

    class Meta:
        model = UserPhone
        fields = BaseSocialSerializer.Meta.fields + ['phone_number']


# - - - - - - - - - - - - - - - USER BANK - - - - - - - - - - - - - - - - -
class UserBankAccountSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    back_account = serializers.IntegerField()

    class Meta:
        model = UserBankAccount
        fields = BaseSocialSerializer.Meta.fields + ['back_account']


class UserBankCartSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    back_cart = serializers.IntegerField()

    class Meta:
        model = UserBankCart
        fields = BaseSocialSerializer.Meta.fields + ['back_cart']


# - - - - - - - - - - - - - - - USER PRODUCT - - - - - - - - - - - - - - - - -
class UserProductSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = BaseSocialSerializer.Meta.fields + ['description', 'image', 'visit_website_url_name',
                                                     'visit_website_url_url']


# - - - - - - - - - - - - - - - USER IMAGE - - - - - - - - - - - - - - - - -
class UserImageSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = BaseSocialSerializer.Meta.fields + ['image']


# - - - - - - - - - - - - - - - USER VIDEO - - - - - - - - - - - - - - - - -
class UserVideoSerializer(BaseSocialSerializer, serializers.ModelSerializer):
    class Meta:
        model = UserVideo
        fields = BaseSocialSerializer.Meta.fields + ['url']


class UserQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'qr_code_url',)
