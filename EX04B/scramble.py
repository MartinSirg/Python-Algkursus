"""Word scrambler."""
import string


def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    sentence_list = sentence.split()
    new_list = []
    for i in range(len(sentence_list)):
        new_list.append(scramble_word(sentence_list[i]))
    new_list = " ".join(new_list)
    return new_list


def scramble_word(word: str):
    """
    Sort a word alphabetically, keeping only the astrophe, first and last letter as they were.

    If the last letter of a word is a symbol (.,;?!") the second to last letter must remain the same.
    If the length of the word without symbols is greater than 7 or the word can't be changed from the
    original, the initial word must be returned. When sorting, treat every letter as lowercase.

    :param word: input word
    :return: alphabetically scrambled word
    """
    if word[-1] in string.punctuation:
        if len(word) >= 8:
            return word
        elif len(word) <= 4:
            return word
        else:
            if "'" in word:                             # Keeping the "'" in the same place:
                ap_index = word.find("'")               # 1.Find "'" index
                word_list = list(word)                  # 2.Make the word into a list
                word_list.remove("'")                   # 3.Remove the "'" from the list
                scrambled = sorted(word_list[1:-2])     # 4.Scramble the required part
                scrambled.insert(ap_index - 1, "'")     # 5.Put the "'" back
                scrambled = "".join(scrambled)
                return word[0] + scrambled + word[-2:]
            else:
                scrambled = sorted(word[1:-2])
                scrambled = "".join(scrambled)
                return word[0] + scrambled + word[-2:]
    elif len(word) >= 7:
        return word
    elif len(word) <= 3:
        return word
    else:
        if "'" in word:
            ap_index = word.find("'")               # 1.Find "'" index
            word_list = list(word)                  # 2.Make the word into a list
            word_list.remove("'")                   # 3.Remove the "'" from the list
            scrambled = sorted(word_list[1:-1])     # 4.Scramble the required part
            scrambled.insert(ap_index - 1, "'")     # 5.Put the "'" back
            scrambled = "".join(scrambled)
            return word[0] + scrambled + word[-1:]
        else:
            scrambled = sorted(word[1:-1])
            scrambled = "".join(scrambled)
            return word[0] + scrambled + word[-1]
