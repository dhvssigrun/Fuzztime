import sys


class PayloadStringList:
    def __init__(self, filename_in):
        self.filename = filename_in
        self.payload_list = []
        self.load_file()

    def load_file(self):
        try:
            file = open(self.filename, 'r')
            for line in file:
                self.payload_list.append(line.strip())
            self.check_data_exists()
            print("{0} payload strings loaded.".format(len(self.payload_list)))
        except IOError:
            print("Payload file not found.")
            sys.exit(1)

    def check_data_exists(self):
        """Ensures that at least one line of payload data is found """
        if len(self.payload_list) == 0:
            print("No data found in payload file.")
            sys.exit(1)
