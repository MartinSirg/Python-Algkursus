"""Dictionary."""
import re
import string

class Dictionary:
    """Work with words and their definitions."""

    def __init__(self, initial_data):
        lines = initial_data.splitlines()
        dictionary = {}
        pattern = re.compile(r"(\([anv]\))([^ 0-9!\"#$%&'()*+,./:;<=>?@[\]^_\-`{|}~\\]+"
                             r"(-?[^ 0-9!\"#$%&'()*+,./:;<=>?@[\]^_\-`{|}~\\]+)?)\s-\s([^ ].*)")
        at_least_1_letter = re.compile(r"[a-zA-Z]+")
        for line in lines:
            match = pattern.match(line)
            if match is not None:
                word_type = match.group(1)
                word = match.group(2).lower()
                definition = match.group(4)
                match_at_least_1_letter = at_least_1_letter.search(word)
                if match_at_least_1_letter is None:
                    continue
                elif word_type + word not in dictionary:
                    dictionary[word_type + word] = [definition]
                else:
                    dictionary[word_type + word].append(definition)
        self.dictionary = dictionary

    def get_definitions(self, word):
        """
        Get all the definitions for a specific word.

        :param word: word to get definitions for
        :return: list of definitions
        """
        result = []
        word = word.lower()
        for key, value in self.dictionary.items():
            if key[3:] == word:
                for item in value:
                    result.append(item)
        return result

    def is_word_noun(self, word):
        word = word.lower()
        for key in self.dictionary.keys():
            if "(n)" + word == key:
                return True
        return False

    def is_word_verb(self, word):
        word = word.lower()
        for key in self.dictionary.keys():
            if "(v)" + word == key:
                return True
        return False

    def is_word_adjective(self, word):
        word = word.lower()
        for key in self.dictionary.keys():
            if "(a)" + word == key:
                return True
        return False

    def get_all_nouns(self):
        result = []
        for key in self.dictionary.keys():
            if key[1] == "n":
                result.append(key[3:])
        return result

    def get_all_verbs(self):
        result = []
        for key in self.dictionary.keys():
            if key[1] == "v":
                result.append(key[3:])
        return result

    def get_all_adjectives(self):
        result = []
        for key in self.dictionary.keys():
            if key[1] == "a":
                result.append(key[3:])
        return result

    def search(self, subword, min_len=0, max_len=999999999999999999999999999999999999999999999999999999999999999999999):
        result = []
        subword = subword.lower()
        for key in self.dictionary.keys():
            if len(key[3:]) > max_len or len(key[3:]) < min_len:
                continue
            elif subword in key and key[3:] not in result:
                result.append(key[3:])
            else:
                continue
        return result


if __name__ == '__main__':
    small_dict_data = "\n".join(["(a)beautiful - very pleasing or satisfying",
                                 "(a)wise - possessed of or characterized by scholarly knowledge or learning",
                                 "(a)kind -",
                                 "(a)Warm - conserving or maintaining warmth or heat",
                                 "(v)Claim - to assert or maintain as a fact",
                                 "(n)ph one - a portable electronic telephone device",
                                 "(a)wise - having the power to judge what is true or right",
                                 "[n]place - a particular portion of space, whether of definite or indefinite exten",
                                 "(a)well-known - clearly or fully known",
                                 "(v)-create - to cause to come into being",
                                 "(n)law - the principles and regulations established in a community by some authority",
                                 "(n)injury - harm or damage that is done or sustained",
                                 "",
                                 "choice - an act or instance of selection",
                                 "(n)fire - a burning mass of material, as on a hearth or in a furnace",
                                 "(b)consume - to destroy or expend by use",
                                 "(v)consume - to eat or drink up; devour",
                                 "(v)fire - to expose to the action of fire; subject to heat",
                                 "(v)¥¥¥ - to inspire"])

    small_dictionary = Dictionary(small_dict_data)

    for key1, value1 in small_dictionary.dictionary.items():
        print(key1 + " : " + str(value1))
