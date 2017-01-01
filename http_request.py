import http.client
import io

from http.server import BaseHTTPRequestHandler


class HttpRequest(BaseHTTPRequestHandler):
    def __init__(self, request_in):
        # self.full_request = repr(request_in.encode("ISO-8859-1"))
        self.rfile = io.StringIO(request_in)
        self.raw_requestline = self.rfile.read()
        print(self.raw_requestline)
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message