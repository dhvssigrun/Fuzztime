import sys


class HttpInputFile:
    def __init__(self, filename_in):
        self.filename = filename_in
        self.content = ""
        self.load_file()

    def load_file(self):
        try:
            file = open(self.filename, 'r')
            self.content = file.read()
            self.check_insertion_point_exists()
        except IOError:
            # todo: handle IOError when opening file
            print("HTTP file not found.")
            sys.exit(1)

    def check_insertion_point_exists(self):
        """Ensures that at least one insertion point exists within a loaded """
        if self.content.find("{0}") == -1:
            print("No {0} insertion point specified.")
            sys.exit(1)
