import os


class ConfigEnv(object):

    def __init__(self):
        self.__load__()

    def __load__(self):
        self.ENVIRONMENT = os.environ.get('ENVIRONMENT', 'localhost')
        self.POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
        self.POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5455')
        self.POSTGRES_USER = os.environ.get('POSTGRES_USER', 'Finkargo')
        self.POSTGRES_PWD = os.environ.get('POSTGRES_PWD', 'Finkargo')
        self.DEBUG = os.environ.get('DEBUG', 'True')
        self.CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6378/0')
        self.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6378/0')
        self.REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6378/0')
        self.MSA_API_URL = os.environ.get('MSA_API_URL', 'http://finkargo-api/v1')
        self.MSA_COMMUNICATOR_URL = os.environ.get('MSA_COMMUNICATOR_URL', 'http://finkargo-communicator/v1')
        self.API_FK_KEY = os.environ.get('API_FK_KEY', 'fb3cbe1285d6')
