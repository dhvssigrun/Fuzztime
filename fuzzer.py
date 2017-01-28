import requests

import fuzz_output

class Fuzzer:
    def __init__(self, target, parameter_list, payload_string_list):
        self.target = target
        self.parameter_list = parameter_list
        self.payload_string_list = payload_string_list
        self.output = []

    def fuzz(self):
        self.generate_http_requests()
        return self.target

    def generate_http_requests(self):
        for payload_string in self.payload_string_list:
            current_parameter_list = {}
            for parameter in self.parameter_list:
                if self.parameter_list[parameter] == "{0}":
                    current_parameter_list[parameter] = payload_string
                else:
                    current_parameter_list[parameter] = self.parameter_list[parameter]

            r = requests.Request('POST', self.target, data=current_parameter_list)
            prepared = r.prepare()

            s = requests.Session()
            s.send(prepared)

            r = requests.post(self.target, data=current_parameter_list, allow_redirects=False)

            self.output.append(fuzz_output.FuzzOutput(payload_string, r.status_code, r.headers,
                                                      r.text))

    @staticmethod
    def pretty_print_post(req):
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in
        this function because it is programmed to be pretty
        printed and may differ from the actual request.
        """
        # https://stackoverflow.com/questions/20658572/python-requests-print-entire-http-request-raw#23816211
        print('{}\n{}\n{}\n\n{}'.format(
            '-----------START-----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            req.body,
        ))
