# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
from pathlib import Path

from temir.conf.env import Env

from django.conf.urls.static import static

BASE_DIR = Path(__file__).resolve().parent


USE_S3 = Env.get('USE_S3') == 'TRUE'

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = Env.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = Env.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = Env.get('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static/'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = (BASE_DIR / 'static/',)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

static_media_root = static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)