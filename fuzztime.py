import http_input_file
import payload_string_list
import fuzzer


def main():
    target = "http://192.168.234.161"
    http_template = http_input_file.HttpInputFile("example_http_request.txt")
    payload_list = payload_string_list.PayloadStringList("example_payload_file.txt")
    fuzzer.Fuzzer(target, http_template.content, payload_list.payload_list)

if __name__ == '__main__':
    main()
