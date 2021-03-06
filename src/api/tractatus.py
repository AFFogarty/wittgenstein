import os
from book import Book

class Tractatus:
    # This is the book
    tractatus = None

    def __init__(self):
        """ Construct the Tractatus """

        # Build the Book object
        self.tractatus = Book()

        # Get the tractatus from text
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        all_text = open(os.path.join(SITE_ROOT, "static", "tractatus.txt"), 'r')
        output = all_text.readlines()

        # Read the file line by line into self.tractatus
        # The actual content only begins at line 30 until the end
        for i in range(30, len(output)):
            complete_string = str(output[i])

            # We need to separate the index and the text
            split_string = complete_string.partition(" ")
            index = split_string[0]
            text = split_string[2].rstrip("\n")

            # Load them in
            self.tractatus.add_section(index, text)

        # print self.tractatus

    def get_book(self):
        return self.tractatus





