import time

from django.conf import settings


class RequestTimeMiddleware:
    '''Miidleware for tracking time of requests'''

    def __init__(self, get_response):
        self.get_response = get_response
        self.file_path = f'{settings.BASE_DIR}/logs/request_time.log'

    def __call__(self, request):
        timestamp = time.monotonic()

        response = self.get_response(request)

        with open(self.file_path, 'a') as file:
            file.write(
                f'{time.monotonic()} - Продолжительность запроса {request.path} - '
                f'{time.monotonic() - timestamp:.3f} сек.\n'
            )
        return response
