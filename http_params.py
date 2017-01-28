import sys


class HttpParams:
    def __init__(self):
        self.content = ""
        self.parameters = {}

    def load_from_file(self, filename_in):
        """Takes a file and splits it"""
        try:
            file = open(filename_in, 'r')
            for line in file:
                self.content += line
                self.separate_params(line)
            # print(self.parameters)
            self.check_insertion_point_exists()
        except IOError:
            # todo: handle IOError when opening file
            print("HTTP file not found.")
            sys.exit(1)

    def load_from_string_list(self, string_list_in):
        """Takes a string and splits it"""
        # print(string_list_in)
        string_split = string_list_in.split('\r\n')
        for line in string_split:
            self.separate_params(line)
        self.check_insertion_point_exists()

    def separate_params(self, line_in):
        split_line = line_in.strip().split("=")
        if len(split_line) >= 2:
            """line_in contains an ="""
            self.parameters[split_line[0]] = split_line[1]

    def check_insertion_point_exists(self):
        """Ensures that at least one insertion point exists within a loaded """
        insertion_point_exists = False
        for parameter in self.parameters:
            if self.parameters[parameter] == "{0}":
                insertion_point_exists = True
        if not insertion_point_exists:
            print("No {0} insertion point specified.")
            sys.exit(1)

