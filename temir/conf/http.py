from temir.conf.env import Env

ALLOWED_HOSTS = Env.get("ALLOWED_HOSTS", '*').split(' ')

# SECURITY WARNING: don't run with debug turned on in production!

CSRF_TRUSTED_ORIGINS = [
    "http://64.227.177.107:8000",
    "http://3.28.174.168",
    "https://temirdata.me"
]

# CORS

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://3.28.174.168",
    "http://64.227.177.107:8000",
    "https://temirdata.me",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
]

if Env.get('DEBUG'):
    ABSOLUTE_HOST = 'http://localhost:3000'
else:
    ABSOLUTE_HOST = 'https://your.app.com'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'ORDERING_PARAM': 'ordering',
}
