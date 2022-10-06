from rest_framework import viewsets, mixins
from {{cookiecutter.app_name}}.adapters.models.sql.{{cookiecutter.endpoint_name}} import {{cookiecutter.endpoint_class}}
from {{cookiecutter.app_name}}.serializers.{{cookiecutter.endpoint_name}} import {{cookiecutter.endpoint_class}}Serializer


class {{cookiecutter.endpoint_class}}ViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = {{cookiecutter.endpoint_class}}.objects.all()
    serializer_class = {{cookiecutter.endpoint_class}}Serializer
