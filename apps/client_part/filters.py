from distutils.util import strtobool

import django_filters
from django_filters import rest_framework as filters

from apps.companies.models import UserCompany
from apps.socials.models import UserBankAccount, UserBankCart
from apps.socials.models.social_models import UserProduct, UserEmail, UserSocial, UserMessanger, UserPhone, UserImage, \
    UserVideo


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    ...


class UserProductFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserProduct
        fields = ['user', ]


class UserEmailFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserEmail
        fields = ['user', ]


class UserSocialFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserSocial
        fields = ['user', ]


class UserMessangerFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserMessanger
        fields = ['user', ]


class UserPhoneFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserPhone
        fields = ['user', ]


class UserBankAccountFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserBankAccount
        fields = ['user', ]


class UserBankCartFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserBankCart
        fields = ['user', ]


class UserImageFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:

        model = UserImage
        fields = ['user', ]


class UserVideoFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserVideo
        fields = ['user', ]


class UserCompanyFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user', lookup_expr='in')

    class Meta:
        model = UserCompany
        fields = ['user', ]