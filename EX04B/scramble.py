"""Word scrambler."""

def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    sentence_list = sentence.split()
    pass


def scramble_word(word: str) -> str:
    """
    Sort a word alphabetically, keeping only the astrophe, first and last letter as they were.

    If the last letter of a word is a symbol (.,;?!") the second to last letter must remain the same.
    If the length of the word without symbols is greater than 7 or the word can't be changed from the
    original, the initial word must be returned. When sorting, treat every letter as lowercase.

    :param word: input word
    :return: alphabetically scrambled word
    """
    pass