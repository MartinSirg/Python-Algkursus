"""Sort the strings in ascending order."""


def sort_list(string_list):
    """
    Function to sort string_list by the length of it's elements.

    This function must utilize get_min_len_word().

    :param string_list: List of Strings to be sorted.
    :return: Sorted list of Strings.
    """
    new_list = string_list
    new_list.sort(key=len)
    return new_list


def get_min_len_word(string_list):
    """
    Function to find and return the minimum length word in string_list.

    If two Strings are the same length, the String appearing first must also
    be returned first.

    :param string_list: List of Strings to look through.
    :return: Smallest length String from string_list.
    """
    new_list = string_list
    new_list.sort(key=len)
    present_list = [new_list[0]]
    for i in range(1, len(new_list), 1):
        if len(new_list[i]) == len(new_list[0]):
            present_list.append(new_list[i])
        else:
            break

    return present_list
