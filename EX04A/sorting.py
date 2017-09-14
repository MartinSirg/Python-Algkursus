"""Sort the strings in ascending order."""


def get_min_len_word(string_list):
    """
    Function to find and return the minimum length word in string_list.

    If two Strings are the same length, the String appearing first must also
    be returned first.

    :param string_list: List of Strings to look through.
    :return: Smallest length String from string_list.
    """
    new_list = string_list
    if len(new_list) == 0:
        return None

    return min(new_list, key=len)


def sort_list(string_list):
    """
    Function to sort string_list by the length of it's elements.

    This function must utilize get_min_len_word().

    :param string_list: List of Strings to be sorted.
    :return: Sorted list of Strings.
    """
    new_list = string_list
    new_list.sort(key=len)
    return [get_min_len_word(string_list)] + new_list[1:len(new_list)]

print(get_min_len_word(['sdaad', 'dsadasd', 'sdsadafgsd','viiis']))
print(sort_list(['sdaad', 'dsadasd', 'sdsadafgsd','viiis']))
print(sort_list(["THIS", 'PROBLEM', "HAS", "ME", 'LIKE', 'PLS', 'Kill', 'ME', 'NOW']))