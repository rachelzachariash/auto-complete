from data import Data
from search import Search
from offline import Offline

# the user insert his sentence and enter to complete the word
class SearchInput:
    def __init__(self):
        self.search = Search()
    # first update the data in offline time then run in a loop and getting a start of sentence from the user and
    # searching for it
    def run(self):
        offline = Offline()
        offline.extract_data("python-3.8.4-docs-text")
        temp = ""
        while True:
            str_to_search = input("search >> {}".format(temp))
            if "#" in str_to_search:
                temp = ""
                str_to_search = ""
            temp += str_to_search
            res = self.search.search(offline.pure_string(temp))
            if res =="End":
                temp = ""

# main function that start the program to run
if __name__ == '__main__':
    SearchInput().run()