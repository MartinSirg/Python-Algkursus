"""Turn a phrase into acronym."""


def acronymize(message: str) -> str:
    """
    Turn the input text into the acronym and reverse it, if the text is not too long.

    :param message: initial text
    :return: reversed acronym
    """
    msg_list = message.split()
    if check_message_length(msg_list) is False:
        return "Sorry, the input's just too long!"
    acronym = ""
    for i in range(len(msg_list)):
        if check_word(msg_list[i]) is True:
            acronym += msg_list[i][0].upper()
    return acronym


def check_word(word: str) -> bool:
    """
    Check if the word is long enough and does not contain special symbols.

    The word should be more than 3 chars long (without symbols).
    There should not be any symbols between the letters
    :param word: word
    :return: bool
    """
    symbols = "()1234567890!?_@#$%^&*.,'"
    string1 = ""
    for i in range(len(word)):
        if word[i] not in symbols:
            string1 += word[i]
    if len(string1) < 4:
        return False
    else:
        string2 = ""
        for i in range(len(word) - 1):
            string2 += word[i]
            if string2[i - 1] in symbols and string2[i] not in symbols:
                result = False
                break
            else:
                result = True
        return result


def check_message_length(words: list) -> bool:
    """
    Check if the initial text length is OK (does not contain more than 50 words).

    :param words: list of words
    :return: bool
    """

    if len(words) > 50:
        return False
    else:
        return True


def reverse(message: str) -> str:
    """
    Reverse the given message.

    :param message: acronym
    :return: reversed message
    """
    if message == "Sorry, the input's just too long!":
        return message
    else:
        new_msg = message[::-1]
        return new_msg
