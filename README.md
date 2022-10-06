# cookiecutter_django_rest_framework

Este repositorio servira como témplate para los proyectos que se deban desarrollar en Django rest-framework, contiene la estructura básica del proyecto en la cual encontraras conexión a base de datos SQL, configuración y conexión a Redis, configuración y conexión a Celery (Worker y Beat).

Para realizar uso del template se debe realizar los siguientes pasos:

1.	Instalar cookiecutter

`pip3 install cookiecutter`

2.	Ejecutar el comando de cookiecutter con el link del template

`cookiecutter https://github.com/StevenLVI/cookiecutter_django_rest_framework.git`

3.	Configurar las variables que solicita cookiecutter

```
project_name -> nombre del proyecto, ejem: msa_test
app_name -> nombre del app que estamos creando,  ejem: test
directory_name -> nombre del directorio principal, ejem: test
endpoint_name -> nombre del endpoint de ejemplo (minusculas),  ejem: category
endpoint_class -> nombre del de la clase para el endpoint de ejemplo (camelcase), ejem: Category
```

4.	Buscamos el archivo `{{ directory_name}}/templates/swagger-ui.html` y en la línea 12 agregamos el siguiente script:

```
    <script>
    const ui = SwaggerUIBundle({
        url: "{% url schema_url %}",
        dom_id: '#swagger-ui',
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "BaseLayout",
        requestInterceptor: (request) => {
          request.headers['X-CSRFToken'] = "{{ csrf_token }}"
          return request;
        }
      })
    </script>
```

Se recomienda que app_name y directory_name tengan el mismo valor para evitar conflictos, cabe aclarar que el valor que pongamos en app_name será también el valor que le daremos a nuestra base de datos.