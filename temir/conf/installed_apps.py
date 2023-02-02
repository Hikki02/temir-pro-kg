INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # lib
    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_yasg',
    'rest_framework_simplejwt',
    'django_rest_passwordreset',
    # 'upload',
    # 'storages',

    # apps
    'apps.users',
    'apps.socials',
    'apps.companies',
    'apps.products',
    'apps.orders',
    'apps.applications',
]
