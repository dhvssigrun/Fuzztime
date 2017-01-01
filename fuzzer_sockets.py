import socket

from urllib.parse import urlparse


class Fuzzer:
    def __init__(self, target, http_request_template, payload_string_list):
        self.target = target
        self.http_request_template = http_request_template
        self.payload_string_list = payload_string_list
        self.generate_http_requests()

    def generate_http_requests(self):
        for payload_string in self.payload_string_list:
            http_request = self.http_request_template.replace("{0}", payload_string)
            self.make_request(http_request, payload_string)

    def make_request(self, http_request, payload_string):
        s = socket.socket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        parsed_url = urlparse(self.target)
        host = parsed_url.netloc

        if parsed_url.scheme == "https":
            port = 443
        else:
            port = 80

        s.connect((host, port))
        # print(http_request)
        s.send(bytes(http_request, encoding="utf-8"))
        received = s.recv(2048).decode("utf-8")
        received_split = received.split('\r\n')
        print('{0}: {1} # Response length: {2}'.format(payload_string, received_split[0], len(received)))
        print(received)
