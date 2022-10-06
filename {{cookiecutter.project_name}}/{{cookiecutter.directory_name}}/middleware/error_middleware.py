import logging
import traceback
from django.http import JsonResponse
from {{cookiecutter.app_name}}.utils.exceptions import (NotImplementedError, BadRequestError)


class ErrorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    logger = logging.getLogger(__name__)

    def process_exception(self, request, exception):
        self.logger.debug("exception={}".format(exception))
        if type(exception) in [NotImplementedError, BadRequestError]:  # Registrar Exceptions
            status = getattr(exception, 'status', None)
            return JsonResponse({'message': str(exception)}, status=status or 422)
        # Registrar bugs!
        trace = traceback.format_exc()
        print(trace)
        return JsonResponse({'message': 'internal server error'}, status=500)

    def __call__(self, request):
        response = self.get_response(request)
        return response
