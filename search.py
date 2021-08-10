from data import Data

# get string and search where the string is a sub string for a sentence
class Search:

    def __init__(self):
        self.data = Data()
        self.sentence = []
    # send string and search where the string contains in a sentence and get a list and return 5 sentences
    def search(self, string):
        if len(string) == 0:
            return
        self.sentence = self.data.search(string)
        for i in range(min(5, len(self.sentence))):
            print(self.sentence[i])
        if len(self.sentence) == 0:
            print("Good results were not found")
            return "End"
        self.sentence = []


    def add_sentence(self, sentence):
        self.sentence.append(sentence)