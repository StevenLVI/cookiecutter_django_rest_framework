from injector import Injector,  singleton, CallableProvider

from {{cookiecutter.app_name}}.adapters.clients.internal.msa_api.users import UsersClient, factory_users_client
from {{cookiecutter.app_name}}.services.internal.users import UsersService


def configure(binder):
    # Servicios
    binder.bind(UsersService, to=UsersService, scope=singleton)

    # Clientes
    binder.bind(UsersClient, to=CallableProvider(factory_users_client))


default_injector = Injector(configure)
