"""Title hehehe."""
import string

symbols = "/#$%^&*@0123456789"


def _correct_message(message: str) -> str:
    """
    Correct message.
    Take out all the symbols between spaces, unless they are at the end or in the beginning
    :param message:
    :return:
    """
    msg_list = message.split()
    new_list = []
    for word in msg_list:
        first_section = ""
        last_section = ""
        for i in range(len(word)):      # First section
            if word[i] in symbols:
                first_section += word[i]
            else:
                break
        for i in range(len(word)):
            if word[-i - 1] in symbols:
                last_section = word[-i - 1] + last_section
            else:
                break
        if len(first_section) > 0:
            index1 = len(first_section)
        else:
            index1 = 0
        index2 = len(word) - len(last_section)
        middle_section = word[index1:index2]
        new_mid = ""
        for i in range(len(middle_section)):
            if middle_section[i] not in symbols:
                new_mid += middle_section[i]
        if first_section == last_section and len(new_mid) == 0:
            result_word = first_section
        else:
            result_word = first_section + new_mid + last_section
        new_list.append(result_word)
    return " ".join(new_list)

def _encrypt_message(message, shift):
    """
    Encrypt the message using Caesar's cipher.
    lower case stay lower case
    upper case stays upper case
    symbols stay the same
    space stays space
    :param message:
    :param shift:
    :return:
    """
    if shift >= 26:
        shift %= 26
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]
    message = message.split()
    """for word in message:
        for i in range(len(word)):
            if word[i] in lower:

            if word[i] in upper:

            if word[i] not in string.ascii_letters:

_encrypt_message("KEKEKE KEKEK KEK KEKEK KEKE", 1)"""