from fuzzer import Fuzzer

import http_params
import payload_string_list


class Fuzztime:
    def __init__(self, target_in, parameter_list_in, payload_list_in):
        # print(target_in)
        self.target = target_in
        self.parameter_list = parameter_list_in
        self.payload_list = payload_list_in

    def fuzz(self):
        # target = "http://192.168.234.161/login.php"
        parameter_list = http_params.HttpParams()
        # parameter_list = http_params.HttpParams("example_http_params.txt")
        parameter_list.load_from_string_list(self.parameter_list)
        payload_list = payload_string_list.PayloadStringList("example_payload_file.txt")
        # parsed_request = http_request.HttpRequest(http_template.content)
        # print (parsed_request.command)
        fuzzer = Fuzzer(self.target, parameter_list.parameters, payload_list.payload_list)
        # print("*****************")
        fuzzer.fuzz()
        # print(fuzzer.output)
        return fuzzer.output

if __name__ == '__main__':
    Fuzztime()
