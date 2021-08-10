# class to hold for each sentence in the data all of the information and have the right Functionality for each sentence
class AutoCompleteData:
    # the information for a sentence
    def __init__(self, completed_sentence, source_text, offset):
        self.__completed_sentence = completed_sentence
        self.__source_text = source_text
        self.__offset = offset
        self.__score = -1

    def get_completed_sentence(self):
        return self.__completed_sentence

    def __str__(self):
        return "{} ({} {} sorce: {})".format(self.__completed_sentence, self.__source_text, self.__offset, self.__score)

    def __lt__(self, other):
        return self.__completed_sentence < other.__completed_sentence

    def set_score(self, score):
        self.__score = score