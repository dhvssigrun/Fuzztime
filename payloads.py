import sys


class Payloads:
    def __init__(self):
        self.payload_list = []

    def load_from_file(self, filename_in):
        try:
            file = open(filename_in, 'r')
            for line in file:
                self.payload_list.append(line.strip())
            self.check_data_exists()
            print("{0} payload strings loaded.".format(len(self.payload_list)))
        except IOError:
            print("Payload file not found.")
            sys.exit(1)

    def load_from_string_list(self, string_list_in):
        string_split = string_list_in.split('\r\n')
        for line in string_split:
            if line != '':
                self.payload_list.append(line)
        self.check_data_exists()

    def check_data_exists(self):
        """Ensures that at least one line of payload data is found """
        if len(self.payload_list) == 0:
            print("No data found in payload file.")
            sys.exit(1)
