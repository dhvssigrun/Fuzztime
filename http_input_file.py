import sys


class HttpInputFile:
    def __init__(self, filename_in):
        self.filename = filename_in
        self.content = ""
        self.parameters = {}
        self.load_file()

    def load_file(self):
        try:
            file = open(self.filename, 'r')
            for line in file:
                self.content += line
                self.separate_params(line)
            print(self.parameters)
            self.check_insertion_point_exists()
        except IOError:
            # todo: handle IOError when opening file
            print("HTTP file not found.")
            sys.exit(1)

    def separate_params(self, line_in):
        split_line = line_in.strip().split("=")
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

