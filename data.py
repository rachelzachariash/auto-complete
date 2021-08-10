# singleton class that implement the program database
import json


class Data:
    __init = False
    __instance = None

    # override new build in function
    def __new__(cls, *args, **kwargs):
        if not Data.__instance:
            Data.__instance = object.__new__(cls)
        return Data.__instance

    # class constructor
    def __init__(self):
        if Data.__init == False:
            self.__autoComplete_collection = {}
            self.__autoComplete_trie = {"list": []}
            Data.__init = True

    # update the autoComplete collection
    def push_autoComplete_collection(self, id, autoComplete):
        self.__autoComplete_collection.update({id: autoComplete})

    # add a string to the trie
    def add_string_to_trie(self, string, id):
        temp = self.__autoComplete_trie
        for i in string:
            if temp.get(i) is not None:
                if len(temp["list"]) >= 5:
                    new_list = self.update_list(temp["list"], id)
                    temp["list"] = new_list
                else:
                    if id not in temp["list"]:
                        temp["list"].append(id)
                temp = temp[i]
            else:
                temp.update({i: {"list": [id]}})
                temp = temp[i]

    # return the autoComplete collection
    def get_autoComplete_collection(self):
        return self.__autoComplete_collection

    def read_file(self):
        with open("trie.json", "r") as f:
            self.__autoComplete_trie = json.load(f)

    # return the autoComplete trie
    def get_autoComplete_trie(self):
        return self.__autoComplete_trie

    # return list of the five highest sentences lexicographical of the 6 given sentences
    def update_list(self, lst, id):
        if len(lst) == 5:
            list_to_return = []
            list_sentence = []
            for i in lst:
                list_sentence.append(self.__autoComplete_collection[i].get_completed_sentence())
            list_sentence.sort()
            new_sentence = self.__autoComplete_collection[id].get_completed_sentence()
            if new_sentence in list_sentence:
                return lst
            if new_sentence < list_sentence[-1]:
                list_sentence.pop()
                for i in lst:
                    if self.__autoComplete_collection[i].get_completed_sentence() in list_sentence:
                        list_to_return.append(i)
                list_to_return.append(id)
            else:
                list_to_return = lst
            return list_to_return
        else:
            return lst
    def update_score_sentence_found(self,score,string_to_find,len_string):
        list_found = self.simple_search(string_to_find, self.__autoComplete_trie)
        for i in range(len(list_found)):
            sentence = self.__autoComplete_collection.get(list_found[i])
            sentence.set_score(2 * len_string - score)
            list_found[i] = sentence
        return list_found

    # search for sentence that the given string with all the type of manipulation is a sub string of the sentence
    def try_derivation(self,string,num_missing):
        list_return=[]
        all_letters='abcdefghijklmnopqrstuvwhyz'
        # change a letter with a different one
        for i in range (len(string)):
            num_latter_manipulation=len(string)-i-1
            if num_latter_manipulation>3:
                for j in all_letters:
                    if num_latter_manipulation-3<len(string):
                        string_to_find=string[:num_latter_manipulation]+j+string[num_latter_manipulation+2:]
                    else:
                        string_to_find = string[:i] + j
                    list_return+= self.update_score_sentence_found(1,string_to_find,len(string) )
                    if len(list_return)>=num_missing:
                        return list_return
        # take off the letter
        for i in range (len(string)):
            num_latter_manipulation=len(string)-i-1
            string_to_find = string[:num_latter_manipulation] + string[num_latter_manipulation + 2:]
            list_return += self.update_score_sentence_found(2,string_to_find,len(string))
            if len(list_return) >= num_missing:
                return list_return
            if num_latter_manipulation>2:
                for j in all_letters:
                    if num_latter_manipulation-2<len(string):
                        string_to_find=string[:num_latter_manipulation]+j+string[num_latter_manipulation+1:]
                    else:
                        string_to_find = string + j
                    list_return += self.update_score_sentence_found(2, string_to_find, len(string))
                    if len(list_return)>=num_missing:
                        return list_return





    # search for the given string or strings with small distance to the given string, in the database
    def search(self, string):
        contain_all_string=True
        prev = self.__autoComplete_trie
        current = self.__autoComplete_trie
        for i in range(len(string)):
            current = prev.get(string[i])
            if current is None:
                contain_all_string = False
                return self.derivation(prev, string[i::], i, len(string))
            prev = current
        sentences = []
        ids = current["list"]

        for i in range(len(ids)):
            sentences.append(self.__autoComplete_collection.get(ids[i]))
            sentences[i].set_score(2 * len(string))
        if len(ids) < 5 and contain_all_string:
            missing_sentence = 5 - len(ids)
            new_sentences = self.try_derivation(string, missing_sentence)
            if new_sentences is not None:
                sentences += new_sentences
        return sentences


    def derivation(self, prev, sub_string, location, string_len):
        sentences_to_return = []
        prev_keys = list(prev.keys())
        prev_keys.remove("list")
        for key in prev_keys:
            if key != sub_string[0]:
                # replace char
                score = (2 * string_len) - (5 - min(4, location))
                sentences_to_return += self.derivation_helper(prev, key, sub_string[1::], score)
            for key in prev_keys:
                if key != sub_string[0]:
                    # add char
                    score = (2 * string_len) - (10 - min(8, 2 * location))
                    sentences_to_return += self.derivation_helper(prev, key, sub_string, score)
        if len(sentences_to_return) < 5:
            # remove char
            if len(sub_string) >= 2:
                current = prev.get(sub_string[1])
                score = (2 * string_len) - (10 - min(8, 2 * location))
                sentences_to_return += self.derivation_helper(prev, sub_string[1], sub_string[2::], score)
        return [item[1] for item in sorted(sentences_to_return, key=lambda x: (-x[0], x[1]))]

    # search for string in the rtie
    def simple_search(self, string, root):
        if root is None:
            return []
        for i in range(len(string)):
            root = root.get(string[i])
            if root is None:
                return []
        my_root=root["list"][::]
        return my_root

    # search after derivation helper
    def derivation_helper(self, root, key, sub_string, score):
        sentences_to_return = []
        temp = self.simple_search(sub_string, root.get(key))
        if temp is not None:
            for i in range(len(temp)):
                if [score, self.__autoComplete_collection.get(temp[i])] not in sentences_to_return:
                    sentences_to_return.append([score, self.__autoComplete_collection.get(temp[i])])
                    sentences_to_return[-1][1].set_score(score)
        return sentences_to_return
    def save(self):
        with open("trie.json","w") as f:
            json.dump(self.__autoComplete_trie, f)
