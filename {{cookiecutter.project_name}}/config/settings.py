from . import SETUP
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%673^1pu7ook&vhvgoo*l(#(ji!p+r424cvejsws%intfprglq'

DEBUG = bool(SETUP.DEBUG)

ALLOWED_HOSTS = []

# Celery settings
CELERYD_APPS = ['{{cookiecutter.app_name}}.tasks.celery.CeleryAppConfig']
CELERYD__BEAT_APPS = ['{{cookiecutter.app_name}}.tasks.celery.CeleryAppConfigBeat']
CELERY_BROKER_URL = SETUP.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = SETUP.CELERY_RESULT_BACKEND
REDIS_URL = SETUP.CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters'
]
THIRD_PARTY_APPS = [
    'django_injector',
    'rest_framework',
    # Health check
    'health_check',
    'health_check.db',
    'health_check.contrib.migrations',
    'health_check.contrib.celery_ping',
    'health_check.contrib.redis',
]

LOCAL_APPS = [
    '{{cookiecutter.app_name}}'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + CELERYD_APPS + CELERYD__BEAT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_injector.inject_request_middleware',


    # Custom
    '{{cookiecutter.app_name}}.middleware.error_middleware.ErrorMiddleware',
]
if SETUP.ENVIRONMENT in ['localhost']:
    MIDDLEWARE += ['{{cookiecutter.app_name}}.middleware.sql_middleware.SqlPrintingMiddleware']


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.app_name}}',
        'USER': SETUP.POSTGRES_USER,
        'PASSWORD': SETUP.POSTGRES_PWD,
        'HOST': SETUP.POSTGRES_HOST,
        'PORT': SETUP.POSTGRES_PORT,
    }
}

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
