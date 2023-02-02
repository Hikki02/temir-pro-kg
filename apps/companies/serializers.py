
from rest_framework import serializers

from apps.companies.models import UserCompany


class UserCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCompany
        fields = ('id', 'user', 'name', 'activity', 'image', 'description', 'visit_website_url_name',
                  'visit_website_url', 'address_url', 'is_main',)

