from werkzeug.wrappers import Request

class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        return self.app(environ, start_response)