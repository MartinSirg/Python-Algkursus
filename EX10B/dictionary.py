"""Dictionary."""
import re


class Dictionary:
    """Work with words and their definitions."""

    def __init__(self, initial_data):
        lines = initial_data.splitlines()
        dictionary = {}
        symbols = "0123456789!\"#$%&'()*+,./:;<=>?@[\]\^_\-`{|}~\\"
        pattern = re.compile(r"(\([anv]\))([^ 0-9!\"#$%&'()*+,./:;<=>?@[\]^_\-`{|}~\\]+"
                             r"(-?[^ 0-9!\"#$%&'()*+,./:;<=>?@[\]^_\-`{|}~\\]+)?)\s-\s([^ ].*)")
        for line in lines:   # TODO [a-zA-Z] doesnt work, must use exception for banned symbols
            match = pattern.match(line)
            if match is not None:
                word_type = match.group(1)
                word = match.group(2).lower()
                definition = match.group(4)
                if word_type + word not in dictionary:
                    dictionary[word_type + word] = [definition]
                else:
                    dictionary[word_type + word].append(definition)
        self.dictionary = dictionary

    def get_definitions(self, word):
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
            elif subword in key:
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
                                 "(v)fire - to inspire"])

    small_dictionary = Dictionary(small_dict_data)

    assert len(small_dictionary.get_definitions("kind")) == 0
    assert len(small_dictionary.get_definitions("phone")) == 0
    assert len(small_dictionary.get_definitions("ph one")) == 0
    assert len(small_dictionary.get_definitions("choice")) == 0
    assert len(small_dictionary.get_definitions("-create")) == 0
    assert len(small_dictionary.get_definitions("create")) == 0
    assert len(small_dictionary.get_definitions("beautiful")) == 1
    assert len(small_dictionary.get_definitions("fire")) == 3
    assert len(small_dictionary.get_definitions("Consume")) == 1
    assert len(small_dictionary.get_definitions("wise")) == 2
    assert small_dictionary.is_word_noun("fire") is True
    assert small_dictionary.is_word_verb("fire") is True
    assert small_dictionary.is_word_adjective('warm') is True
    assert small_dictionary.is_word_noun("place") is False

    all_nouns = small_dictionary.get_all_nouns()
    assert isinstance(all_nouns, list)

    assert len(all_nouns) == 3
    assert "law" in all_nouns
    assert "injury" in all_nouns
    assert "fire" in all_nouns

    all_verbs = small_dictionary.get_all_verbs()
    assert isinstance(all_verbs, list)

    assert len(all_verbs) == 3
    assert "consume" in all_verbs
    assert "claim" in all_verbs
    assert "fire" in all_verbs

    all_adjectives = small_dictionary.get_all_adjectives()
    assert isinstance(all_adjectives, list)

    assert len(all_adjectives) == 4
    assert "wise" in all_adjectives
    assert "warm" in all_adjectives
    assert "beautiful" in all_adjectives
    assert "well-known" in all_adjectives

    search_result = small_dictionary.search("N", min_len=5, max_len=8)
    assert len(search_result) == 2
    assert 'consume' in search_result
    assert 'injury' in search_result
    for keyo, valueo in small_dictionary.dictionary.items():
        print(keyo + " : " + str(valueo))
    print(type(small_dictionary.dictionary.values()), end=" ")
    print("  <== Ei tagasta <class 'list'> hah ")
