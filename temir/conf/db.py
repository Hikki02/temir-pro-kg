from pathlib import Path

from temir.conf.env import Env

BASE_DIR = Path(__file__).resolve().parent.parent
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': Env.get('SQL_ENGINE'),
        'NAME': Env.get('SQL_DATABASE'),
        'USER': Env.get('SQL_USER'),
        'PASSWORD': Env.get('SQL_PASSWORD'),
        'HOST': Env.get('SQL_HOST'),
        'PORT': Env.get('SQL_PORT'),
        
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
