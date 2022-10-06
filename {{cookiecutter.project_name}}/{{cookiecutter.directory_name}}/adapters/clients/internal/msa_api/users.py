from config import SETUP
from unittest.mock import MagicMock

from {{cookiecutter.app_name}}.constanst import LOCALHOST_ENV
from {{cookiecutter.app_name}}.adapters.clients.internal.base import ClientBase


class UsersClient(ClientBase):
    def __init__(self, **args):
        super().__init__(**args)

    def get_user(self, id_user: int) -> dict:
        self.__get_user(id_user)

    def __get_user(self, id_user: int) -> dict:
        url = self.get_url('users/%i' % id_user)
        return self.consume_request(url=url)


def __mock_get_user(id_user: int):
    print("==== MOCK GET USER %i ===" % id_user)
    return {
        "id_user": id_user,
        "name": 'John',
        "surname": 'Doe',
        "email": 'john.doe@finkargo.com',
        "role": "admin"
    }


def factory_users_client():
    client = UsersClient()
    if SETUP.ENVIRONMENT in [LOCALHOST_ENV]:
        client.get_user = MagicMock(side_effect=__mock_get_user)
    return client
