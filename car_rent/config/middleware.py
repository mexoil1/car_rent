import time


class RequestTimeMiddleware:
    '''Miidleware for tracking time of requests'''

    def __init__(self, get_response):
        self.get_response = get_response
        self.file_path = 'logs/request_time.log'

    def __call__(self, request):
        timestamp = time.monotonic()

        response = self.get_response(request)

        with open(self.file_path, 'a') as file:
            file.write(
                f'{time.monotonic()} - Продолжительность запроса {request.path} - '
                f'{time.monotonic() - timestamp:.3f} сек.\n'
            )
        return response
