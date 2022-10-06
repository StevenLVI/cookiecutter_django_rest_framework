from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

schema_url_patterns = [
    path('v1/', include(('{{cookiecutter.app_name}}.ports.urls', '{{cookiecutter.app_name}}'), namespace='{{cookiecutter.app_name}}'))
]

urlpatterns = [
    path('openapi', get_schema_view(
        title="{{cookiecutter.app_name}}",
        description="API para cartera",
        version="2.0.0",
        patterns=schema_url_patterns
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('v1/healthcheck', include('health_check.urls')),
    *schema_url_patterns
]
