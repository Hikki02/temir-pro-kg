from rest_framework import serializers

from apps.companies.models import UserCompany
from apps.companies.serializers import UserCompanySerializer
from apps.socials.serializers import UserImageSerializer, UserPhoneSerializer, UserSocialSerializer, \
    UserEmailSerializer, UserImage, UserMessangerSerializer
from apps.users.models import User, SaveContactCount
from temir.settings import SITE_URL


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'number_of_gold_user', 'password')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if validated_data['password']:
            user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password')


class UserSaveContactSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()
    user_avatar = serializers.SerializerMethodField()
    user_images = UserImageSerializer(many=True)
    user_phone = UserPhoneSerializer(many=True)
    user_social = UserSocialSerializer(many=True)
    user_email = UserEmailSerializer(many=True)
    user_url = serializers.SerializerMethodField()

    user_messanger = UserMessangerSerializer(many=True)

    user_company = UserCompanySerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'work_phone', 'website',
                  'personal_phone', 'work_email', 'email', 'full_name',
                  'user_url',
                  'user_messanger',
                  'avatar',
                  'background',
                  'position',
                  'company_name',
                  'user_social',
                  'user_avatar',
                  'user_images', 'user_phone', 'user_email',
                  'user_company'
                  )

    def get_company_name(self, obj):
        try:
            company = UserCompany.objects.filter(user=obj.user_company.filter(is_main=True).name)
            return company
        except:
            return None

    def get_user_avatar(self, obj):
        try:
            avatar = UserImage.objects.filter(user=obj.user_images.filter(is_avatar=True).image)
            print('sdfsdfsf', avatar)
            return avatar
        except:
            return None

    def get_full_name(self, obj):
        if obj.first_name == None:
            obj.first_name = ' '
        if obj.last_name == None:
            obj.last_name = ' '
        #        elif obj.first_name and obj.last_name == None:
        #            obj.first_name = ''
        #            obj.last_name = ''
        else:
            first_name = obj.first_name
            last_name = obj.last_name
            full_name = f'{first_name} {last_name}'
            print(full_name)
            return full_name

    def get_user_url(self, obj):
        site_url = SITE_URL
        return site_url


class CreateSaveContactCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveContactCount
        fields = ('user', 'count',)


class SaveContactCountSerializer(serializers.ModelSerializer):
    total_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'total_count')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'avatar', 'background', 'username', 'welcome', 'position', 'work_phone',
            'personal_phone', 'work_email', 'email', 'en_english')


class UserRetrieveSerializer(UserSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ('number_of_gold_user', 'en_english',)
