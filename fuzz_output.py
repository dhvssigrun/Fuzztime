class FuzzOutput:
    def __init__(self, payload_item, return_code, response):
        self.payload_item = payload_item
        self.return_code = return_code
        self.response_length = 0
        self.response = response