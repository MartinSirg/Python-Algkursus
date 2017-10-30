"""Title hehehe."""
import string

symbols = "/#$%^&*@0123456789"


def _correct_message(message: str) -> str:
    """
    Correct message.

    Take out all the symbols between spaces, unless they are at the end or in the beginning.
    Divide the message into three sections:
    1.st section - symbols in the beginning of the word
    2.nd section - text between beginning and end sections
    3.rd section - symbols in the end
    :param message:
    :return:
    """
    msg_list = message.split()
    new_list = []
    for word in msg_list:
        first_section = ""
        last_section = ""
        for i in range(len(word)):                      # Make first section
            if word[i] in symbols:
                first_section += word[i]
            else:
                break
        for i in range(len(word)):                      # Make last section
            if word[-i - 1] in symbols:
                last_section = word[-i - 1] + last_section
            else:
                break
        if len(first_section) > 0:                      # Make middle section with word[index1: index2]
            index1 = len(first_section)                 # Figure out index 1
        else:
            index1 = 0
        index2 = len(word) - len(last_section)          # Figure out index 2
        middle_section = word[index1:index2]            # Define middle section
        new_mid = ""                                    # Soon to be corrected middle section
        for i in range(len(middle_section)):            # Loop through middle
            if middle_section[i] not in symbols:        # Take out all given symbols
                new_mid += middle_section[i]
        if first_section == last_section and len(new_mid) == 0:     # Exception for when a word consists of only symbols
            result_word = first_section
        else:
            result_word = first_section + new_mid + last_section    # Final result of a new word under normal cond.
        new_list.append(result_word)                                # Add new word to list
    return " ".join(new_list)                                       # Join the list together


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
    lower = string.ascii_lowercase                  # Make lower case alphabet string
    upper = string.ascii_uppercase                  # Make upper case alphabet string
    shifted_lower = lower[shift:] + lower[:shift]   # Shift the alphabets
    shifted_upper = upper[shift:] + upper[:shift]
    message = message.split()                       # Message string -> list
    new_message = []                                # Soon ot be filled new message list
    for word in message:
        new_word = ""                               # using index() method: string.index("char")
        for i in range(len(word)):
            if word[i] in lower:                    # When iterable char is lower case
                index = lower.index(word[i])
                new_word += shifted_lower[index]
            elif word[i] in upper:                  # When iterable char is upper case
                index = upper.index(word[i])
                new_word += shifted_upper[index]
            else:                                   # Symbols, numbers and other
                new_word += word[i]
        new_message.append(new_word)
    return " ".join(new_message)


def get_corrected_encrypted_message(initial_message, shift):
    """Correct and encrypt the message using previous functions."""
    fixed_message = _correct_message(initial_message)
    encrypted_message = _encrypt_message(fixed_message, shift)
    return encrypted_message
