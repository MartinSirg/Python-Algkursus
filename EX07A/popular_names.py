"""Order names by popularity."""


def read_from_file() -> list:
    """
    Create the list of all the names.

    :return: list
    """
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names


def to_dictionary(names: list) -> dict:
    """
    Make a dictionary from a list of names.

    :param names: list of all the names
    :return: dictionary {"name:sex": number}
    """
    dictionary = {}
    for i in range(len(names)):
        dictionary[i] = names[i]
    return dictionary


def to_sex_dicts(names_dict: dict) -> tuple:
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    """
    female_counter = 0
    male_counter = 0
    female_names = {}
    male_names = {}
    for i in names_dict:
        if names_dict[i][-1] == "F":
            female_names[female_counter] = names_dict[i][:-2]
            female_counter = female_counter + 1
        else:
            male_names[male_counter] = names_dict[i][:-2]
            male_counter = male_counter + 1
    return female_names, male_names


def most_popular(names_dict: dict) -> str:
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names
    :return: string
    1. https://stackoverflow.com/questions/26871866/print-highest-value-in-dict-with-key
    """
    if len(names_dict) == 0:
        return "Empty dictionary."
    else:
        frequency = names_with_frequency(names_dict)
        most_frequent = max(frequency, key=frequency.get)  # .1
        return most_frequent


def number_of_people(names_dict: dict) -> int:
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names
    :return: int
    """
    return len(names_dict)


def names_by_popularity(names_dict: dict) -> str:
    r"""
    Create a string used to print the names by popularity.

    Format:
        1. name: number of people + "\n"
        ...

    Example:
        1. Kati: 100
        2. Mati: 90
        3. Nati: 80
        ...

    :param names_dict: dictionary of the names
    :return: string
    """
    pass


def names_with_frequency(names_dict):
    list_of_names = []                                      # Make a list for different names
    for i in range(len(names_dict)):                        # Loop through the dictionary of people
        if i == 0:                                          #
            list_of_names.append(names_dict[0][:-2])        # Add the first name in the dictionary to the list
            continue                                        #
        elif names_dict[i][:-2] == names_dict[i - 1][:-2]:  # If current iterable name is same as the last continue
            continue                                        #
        else:                                               #
            list_of_names.append(names_dict[i][:-2])        # If find new name, add to list
    string_names_dict = str(names_dict)                     # Convert dictionary into a long string
    frequency = {}                                          # Dictionary with names and their frequency
    for i in range(len(list_of_names)):                     # Count the number of times a name appears in the string
        frequency[list_of_names[i]] = string_names_dict.count(list_of_names[i])
    return frequency


dictionary1 = to_dictionary(read_from_file())
print(number_of_people(dictionary1))

