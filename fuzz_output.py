import json


class FuzzOutput:
    def __init__(self, payload_item, return_code, headers, body):
        self.payload_item = payload_item
        self.return_code = return_code
        self.headers = json.dumps(dict(headers),
                                  indent=4,
                                  separators=(',', ':'))
        self.headers_length = len(json.dumps(dict(headers)))
        self.body = body
        self.body_length = len(body)
