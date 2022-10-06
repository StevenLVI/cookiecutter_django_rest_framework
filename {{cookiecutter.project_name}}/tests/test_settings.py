from . import SETUP

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]
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
