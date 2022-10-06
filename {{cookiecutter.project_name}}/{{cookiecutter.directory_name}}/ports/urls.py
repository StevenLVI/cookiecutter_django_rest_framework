from django.urls import path
from {{cookiecutter.app_name}}.ports import rest as rs
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'{{cookiecutter.endpoint_name}}', rs.{{cookiecutter.endpoint_class}}ViewSet, basename='{{cookiecutter.endpoint_name}}')

urlpatterns = [
    *router.urls
]