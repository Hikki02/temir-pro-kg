# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'temir.urls'

WSGI_APPLICATION = 'temir.wsgi.application'
