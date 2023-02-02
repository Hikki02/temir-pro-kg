import vobject
from django.contrib.auth.hashers import check_password
from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from slugify import slugify

import base64, requests

from apps.users.models import User, SaveContactCount
from apps.users.serializers import RegistrationSerializer, UserLoginSerializer, UserSaveContactSerializer, \
    SaveContactCountSerializer, CreateSaveContactCountSerializer, UserSerializer, UserRetrieveSerializer
from apps.users.utils import generateError, generateAuthInfo, b64_image, get_as_base64
from temir import settings


class UserCreate(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.filter()
    permission_classes = (IsAuthenticated,)  # need to change to isStaff

    def create(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data={'password': settings.DEFAULT_PASSWORD},
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=f"{settings.SITE_URL}?user={serializer.data['id']}")


class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('id')
        password = request.data.get('password')
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(**generateError('DOES_NOT_EXIST'))
        checkPassword = check_password(password, user.password)
        if not checkPassword:
            return Response(**generateError('WRONG_PASSWORD'))
        serializer = self.serializer_class(user, context={'request': request})
        return Response(data=generateAuthInfo(user, serializer.data))


class UserSaveContact(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSaveContactSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        user = self.queryset.get(id=kwargs[self.lookup_field]);
        user = self.serializer_class(user).data
        vCard = vobject.vCard()



        full_name = vCard.add('url')
        full_name.value = user['website'] if user['website'] else ''

        if user['first_name'] == None:
            user['first_name'] = ''
        if user['last_name'] == None:
            user['last_name'] = ''
        first_name = user['first_name']
        last_name = user['last_name']
        full_name = f'{first_name} {last_name}'


        vCard.add('N;CHARSET=UTF-8').value = full_name if full_name else ''
        vCard.add('fn').value = full_name if full_name else ''

        user_url = f"{user['user_url']}user/{kwargs[self.lookup_field]}"
        vCard.add('url').value = user_url if user_url else ''

        user_messangers = []
        for i in user['user_messanger']:
            social_title = i['title']
            social_url = i['url']
            user_messangers.append((social_title, social_url))

        # social
        for social in user_messangers:
            soc = vCard.add('url')
            soc.type_param = social[0]
            soc.value = social[1]


#        vCard.add('fn').value = user['full_name'] if user['full_name'] else ''
#        vCard.add('N;CHARSET=UTF-8').value = user['full_name'] if user['full_name'] else ''
#        vCard.add('N;CHARSET=UTF-8').value = user['full_name'] if user['full_name'] else ''
#        vCard.add('email').value = user['email'] if user['email'] else ''
        vCard.add('TITLE;CHARSET=UTF-8').value = user['position'] if user['position'] else ''

        for i in user['user_company']:
            if i['is_main'] == True:
                vCard.add('ORG;CHARSET=UTF-8').value = i['name'] if i['name'] else ''
            else:
                vCard.add('ORG;CHARSET=UTF-8').value = ''

        if user['avatar']:
            base64 = get_as_base64(user['avatar'])
            photo = vCard.add(f'PHOTO;ENCODING=b;TYPE=image/{base64}')
            photo.value = base64

        user_socials = []
        for i in user['user_social']:
            social_title = i['title']
            social_url = i['url']
            user_socials.append((social_title, social_url))

        # PHONE
        personal_phone = vCard.add('tel')
        personal_phone.type_param = "CELL"
        personal_phone.value = user['personal_phone'] if user['personal_phone'] else ''

        work_phone = vCard.add('tel')
        work_phone.type_param = 'WORK'
        work_phone.value = user['work_phone'] if user['work_phone'] else ''

        # EMAIL
        personal_email = vCard.add('EMAIL')
        personal_email.type_param = 'CELL'
        personal_email.value = user['email'] if user['email'] else ''

        work_email = vCard.add('EMAIL')
        work_email.type_param = 'WORK'
        work_email.value = user['work_email'] if user['work_email'] else ''

        # social
        for social in user_socials:
            soc = vCard.add('url')
            soc.type_param = social[0]
            soc.value = social[1]

        fullname_slug = slugify(user['full_name']) if user['full_name'] else None
        filename = (fullname_slug or user['work_email']) if (user['full_name'] or user['work_email']) else user['id']
        response = HttpResponse(vCard.serialize(), content_type='text/x-vcard')
        response['Content-Disposition'] = f'attachment; filename={filename}.vcf'
        return response


class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSaveContactSerializer

    def retrieve(self, request, *args, **kwargs):
        vCard = vobject.vCard()
        user = self.queryset.get(id=kwargs[self.lookup_field]);
        user = self.serializer_class(user).data
        vCard = vobject.vCard()

        # print(user.get(['user_company'][0][2]))
        # print(user['user_company'][0]['name'], '')
        # print(user['company_name'])

#        full_name = vCard.add('fn')
#        full_name.type_param = "FN"
#        full_name.value = user['full_name'] if user['full_name'] else ''
        print(user['full_name'])


        vCard.add('fn').value = user['full_name'] if user['full_name'] else ''
        vCard.add('N;CHARSET=UTF-8').value = user['full_name'] if user['full_name'] else ''

        company = vCard.add('org')
        company.value = user.get('company_name', '')
        company.type_param = 'ORG'

        return HttpResponse("ok")


class UserRetrievee(generics.RetrieveAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSaveContactSerializer


class SaveContactCountListAPiView(generics.ListAPIView):
    serializer_class = SaveContactCountSerializer

    def get_queryset(self):
        order = User.objects.filter(). \
            annotate(total_count=Sum('save_contact_user__count'))
        return order


class SaveContactCountRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SaveContactCountSerializer

    def get_queryset(self):
        order = User.objects.filter(). \
            annotate(total_count=Sum('save_contact_user__count'))
        return order


class SaveContactCountCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateSaveContactCountSerializer

    def get_queryset(self):
        order = SaveContactCount.objects.filter()
        return order


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.filter()
