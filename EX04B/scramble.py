"""Word scrambler."""
import string


def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    sentence_as_list = sentence.split()
    new_list = []
    for i in range(len(sentence_as_list)):
        new_list.append(scramble_word(sentence_as_list[i]))
    new_list = " ".join(new_list)
    return new_list


def scramble_word(word: str):
    """
    Sort a word alphabetically, keeping only the apostrophe, first and last letter as they were.

    If the last letter of a word is a symbol (.,;?!") the second to last letter must remain the same.
    If the length of the word without symbols is greater than 7 or the word can't be changed from the
    original, the initial word must be returned. When sorting, treat every letter as lowercase.

    :param word: input word
    :return: alphabetically scrambled word
    """
    if len(word) == 0:
        return ""
    elif word[-1] in string.punctuation:
        if len(word) >= 9 or len(word) <= 4:
            return word
        else:
            if "'" in word:                                         # Keeping the "'" in the same place:
                ap_index = word.find("'")                           # 1.Find "'" index
                word_list = list(word)                              # 2.Make the word into a list
                word_list.remove("'")                               # 3.Remove the "'" from the list
                scrambled = sorted(word_list[1:-2], key=str.lower)  # 4.Scramble the required part
                scrambled.insert(0, word[0])                        # 5.Insert the first letter
                scrambled.append(word[-2:])                         # 6.Insert the last letter
                scrambled.insert(ap_index, "'")                     # 7.Insert the "'"
                scrambled = "".join(scrambled)                      # 8.List --> String
                return scrambled
            else:
                scrambled = sorted(word[1:-2], key=str.lower)
                scrambled.insert(0, word[0])
                scrambled.append(word[-2:])
                scrambled = "".join(scrambled)
                return scrambled
    elif len(word) >= 8 or len(word) <= 3:
        return word
    else:
        if "'" in word:
            ap_index = word.find("'")
            word_list = list(word)
            word_list.remove("'")
            scrambled = sorted(word_list[1:-1], key=str.lower)
            scrambled.insert(0, word[0])
            scrambled.append(word[-1])
            scrambled.insert(ap_index, "'")
            scrambled = "".join(scrambled)
            return scrambled
        else:
            scrambled = sorted(word[1:-1], key=str.lower)
            scrambled.insert(0, word[0])
            scrambled.append(word[-1])
            scrambled = "".join(scrambled)
            return scrambled
