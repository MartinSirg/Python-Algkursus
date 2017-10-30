"""Decrypt message."""
import string
import encoder


def _decrypt_message(encrypted_message, shift):
    """
    Decrypt the message.
    :param encrypted_message: encrypted message
    :param shift: Caesars's cipher's shift
    :return: decrypted message
    """
    if shift >= 26:
        shift %= 26
    lower = string.ascii_lowercase                      # Make lower case alphabet string
    upper = string.ascii_uppercase                      # Make upper case alphabet string
    shifted_lower = lower[shift:] + lower[:shift]       # Shift the alphabets
    shifted_upper = upper[shift:] + upper[:shift]
    encrypted_message = encrypted_message.split()       # decrypted_msg string -> list
    decrypted_message = []                              # Soon to be filled decrypted_message list
    for word in encrypted_message:
        new_word = ""                                   # using index() method: string.index("char")
        for i in range(len(word)):
            if word[i] in lower:                        # When iterable char is lower case
                index = shifted_lower.index(word[i])
                new_word += lower[index]
            elif word[i] in upper:                      # When iterable char is upper case
                index = shifted_upper.index(word[i])
                new_word += upper[index]
            else:                                       # Symbols, numbers and other
                new_word += word[i]
        decrypted_message.append(new_word)
    return " ".join(decrypted_message)


def get_message(initial_message, shift, decrypt=False):
    """
    Correct message and return encrypted or decrypted message
    :param initial_message: uncorrected message
    :param shift: Caesars's cipher's shift
    :param decrypt: if set to True, then message is also decrypted
    :return: encrypted or decrypted message, depending on decrypt parameter
    """
    encrypted_msg = encoder.get_corrected_encrypted_message(initial_message, shift)
    if decrypt is False:
        return encrypted_msg
    else:
        return _decrypt_message(encrypted_msg, shift)
