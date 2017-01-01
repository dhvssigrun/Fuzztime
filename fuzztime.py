import http_input_file
import http_request
import payload_string_list
import fuzzer


def main():
    target = "http://192.168.234.161/login.php"
    parameter_list = http_input_file.HttpInputFile("example_http_params.txt")
    payload_list = payload_string_list.PayloadStringList("example_payload_file.txt")
    # parsed_request = http_request.HttpRequest(http_template.content)
    # print (parsed_request.command)
    fuzzer.Fuzzer(target, parameter_list.parameters, payload_list.payload_list)

if __name__ == '__main__':
    main()
