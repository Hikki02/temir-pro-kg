import base64
import os
from datetime import datetime

from django.conf import settings


# - - - - - - - - - - - - - - - - - UPLOAD PATHS - - - - - - - - - - - - -

def user_image_upload_path(instance, filename):
    return os.path.join('users/avatar/', datetime.now().date().strftime("%Y/%m/%d"), filename)


def user_company_image_upload_path(instance, filename):
    return os.path.join('users/avatar/', datetime.now().date().strftime("%Y/%m/%d"), filename)


from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def generateError(errorCode):
    return {
        'status': status.HTTP_400_BAD_REQUEST,
        'data': {
            'error': True,
            'code': errorCode
        }
    }


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def generateAuthInfo(user, data):
    return {
        **get_tokens_for_user(user),
        'profile': data
    }


def b64_image(filepath):
    try:
        with open(f'{settings.BASE_DIR}{filepath}', 'rb') as f:
            b64 = base64.b64encode(f.read())
            data = {
                "success": True,
                "base64": b64.decode('utf-8'),
                'extension': f.name.split('.')[-1][0],
            }
            f.close()
            return data
    except:
        return {
            "success": False
        }

import base64
import requests

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content).decode('utf-8')