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
    for name in names:
        if name not in dictionary:
            dictionary[name] = 1
        else:
            dictionary[name] += 1
    return dictionary


def to_sex_dicts(names_dict: dict) -> tuple:
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    dictionary iteration: https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
    """
    male_names = {}
    female_names = {}
    for key in names_dict:
        if key[-1] == "F":
            female_names[key[:-2]] = names_dict[key]
        else:
            male_names[key[:-2]] = names_dict[key]
    return male_names, female_names


def most_popular(names_dict: dict) -> str:
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names
    :return: string
    """
    if len(names_dict) == 0:
        return "Empty dictionary."
    highest_value = 0
    highest_key = ""
    for key, value in names_dict.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
        else:
            continue
    return highest_key


def number_of_people(names_dict: dict) -> int:
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names
    :return: int
    """
    number = 0
    for value in names_dict.values():
        number += value
    return number


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
    string = ""
    for i in range(len(names_dict) + 1):
        if i == 0:
            continue
        current_mp = most_popular(names_dict)
        string = string + str(i) + ". " + current_mp + ": " + str(names_dict[current_mp]) + "\n"
        del names_dict[most_popular(names_dict)]
    return string


if __name__ == '__main__':
    example_names = ("Kati:F\n" * 1000 + "Mati:M\n" * 800 + "Mari:F\n" * 600 + "Tõnu:M\n" * 400).rstrip("\n").split("\n")
    people = to_dictionary(example_names)
    print(people)  # -> {'Kati:F': 1000, 'Mati:M': 800, 'Mari:F': 600, 'Tõnu:M': 400}
    male_names, female_names = to_sex_dicts(people)
    print(male_names)  # -> {'Mati': 800, 'Tõnu': 400}
    print(female_names)  # -> {'Kati': 1000, 'Mari': 600}
    print(most_popular(male_names))  # -> "Mati"
    print(number_of_people(people))  # -> 2800
    print(names_by_popularity(male_names))  # ->   1. Mati: 800
#                                                  2. Tõnu: 400
#                                                  (empty line)
    dict1 = to_dictionary(read_from_file())
    print(dict1)
