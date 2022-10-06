from injector import inject

from {{cookiecutter.app_name}}.adapters.clients.internal.msa_api.users import UsersClient


class User:
    id_user = 0
    name = ''
    surname = ''
    email = ''
    rol = ''

    def __init__(self, **kwargs):
        for key in kwargs:
            self.__dict__[key] = kwargs[key]

    def __str__(self) -> str:
        return self.name + ' ' + self.surname


class UsersService(object):
    @inject
    def __init__(self, users_client: UsersClient):
        self.__users_client = users_client

    def get_user(self, id_user: int) -> User:
        args = self.__users_client.get_user(id_user)
        return User(**args)
