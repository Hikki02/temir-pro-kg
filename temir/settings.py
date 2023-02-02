"""
Django settings for temir project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from split_settings.tools import include


from temir.conf.env import Env

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = Env.get("SECRET_KEY")
DEBUG = Env.get("DEBUG", )
DEFAULT_PASSWORD = Env.get("DEFAULT_PASSWORD")
SITE_URL = Env.get('SITE_URL')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

USE_S3 = Env.get('USE_S3') == 'TRUE'

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = Env.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = Env.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = Env.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.me-central-1.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_REGION_NAME = "me-central-1"
    # s3 static settings
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STORAGE_BUCKET_NAME}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    MEDIA_URL = 'media/'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

include(
    'conf/auth.py',
    'conf/boilerplate.py',
    'conf/db.py',
    'conf/http.py',
    'conf/installed_apps.py',
    'conf/middleware.py',
    # 'conf/static_media.py',
    'conf/templates.py',
    'conf/internationalization.py',
    'conf/simple_jwt.py',
)
