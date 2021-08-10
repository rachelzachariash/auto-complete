from data import Data
from autoCompleteData import AutoCompleteData
import os

# in charge sending to the data how to save the data offline that the search will be effective
class Offline:
    # id amount of sentence in that was pouted in the data
    def __init__(self):
        self.__data = Data()
        self.id_counter = 0
    # get root of file read in lines all the file and send for each line (sentence) save the sentence and update it
    # in the trie
    def building_trie_and_dict_autoCompletes(self, source, root, file):
        num_line = 1
        with open(root + "/" + file, "r", encoding='utf8') as f:
            line = f.readline()
            while line:
                line = f.readline()
                string = line[:-1]
                string_for_complete = self.pure_string(string)
                if string_for_complete != "":
                    num_line += 1
                    self.id_counter += 1
                    self.put_strings_for_complete(string_for_complete, source, num_line)
                    # self.put_string_in_trie(string_for_complete)

    def get_data(self):
        return self.__data
    # get sentence and make sure that contains only lower case lattes
    def pure_string(self, sentence):
        mew_sentence = sentence.lower()
        sentence_to_return = ""
        one_space = True
        for i in mew_sentence:
            if 97 <= ord(i) <= 122 or i == " ":
                if i == " " and one_space == True:
                    one_space = False
                    sentence_to_return = sentence_to_return + i
                elif 97 <= ord(i) <= 122:
                    one_space = True
                    sentence_to_return = sentence_to_return + i
        if len(sentence_to_return) > 0 and sentence_to_return[-1] == " ":
            sentence_to_return = sentence_to_return[:-1]
        return sentence_to_return
    # get sentence and put it in DB
    def put_strings_for_complete(self, string_for_complete, source, num_line):
        new_autoComplete = AutoCompleteData(string_for_complete, source, num_line)
        self.__data.push_autoComplete_collection(self.id_counter, new_autoComplete)

    # get sentence and update the trie according to the new sentence
    def put_string_in_trie(self, string_for_complete):
        for i in range(len(string_for_complete)):
            self.__data.add_string_to_trie(string_for_complete[i::], self.id_counter)
    # get a dir and read send all the files with add txt to the read all the sentence from their
    def extract_data(self, dir):
        for root, subdirs, files in os.walk(dir):
            for file in files:
                if file.endswith("txt"):
                    self.building_trie_and_dict_autoCompletes(file[:file.index(".txt")], root, file)
        self.__data.read_file()