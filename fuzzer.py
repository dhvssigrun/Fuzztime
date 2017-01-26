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

            # self.pretty_print_POST(prepared)

            s = requests.Session()
            s.send(prepared)
            # print(s.)

            r = requests.post(self.target, data=current_parameter_list, allow_redirects=False)
            # print(self.target)
            # print(r.prepare())
            # print(r.headers)
            # current_fuzz = fuzz_output.FuzzOutput(payload_string, r.status_code, r.headers)
            # print(type(r.headers))
            self.output.append(fuzz_output.FuzzOutput(payload_string, r.status_code, r.headers,
                                                      r.text))
            # self.output.append('{0}: {1} Response length: {2}\n{3}'.format(payload_string,
            #                                                                r.status_code,
            #                                                                len(r.headers),
            #                                                                r.headers))
            # print(r.headers)
            # print(r.url)
            # print(r.history)
            # print(r.text)
            # http_request = self.http_request_template.replace("{0}", payload_string)
            # self.make_request(http_request, payload_string)
            # return self.output

    def pretty_print_POST(self, req):
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
