from django.db import models
from {{cookiecutter.app_name}}.adapters.models.sql.base import BaseModel


class {{cookiecutter.endpoint_class}}(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False)
    status = models.BooleanField(default=True)