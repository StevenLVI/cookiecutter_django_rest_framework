from {{cookiecutter.app_name}}.adapters.models.sql.{{cookiecutter.endpoint_name}} import {{cookiecutter.endpoint_class}}
from rest_framework import serializers


class {{cookiecutter.endpoint_class}}Serializer(serializers.ModelSerializer):

    class Meta:
        model = {{cookiecutter.endpoint_class}}
        exclude = []
