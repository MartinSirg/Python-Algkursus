"""Main module."""
import acronymator


def get_reversed_acronym(message):
    """
    The main method of the program.

    :param message: initial text
    :return: reversed acronym of the given message
    """
    acronym = acronymator.acronymize(message)
    reversed_acronym = acronymator.reverse(acronym)
    return reversed_acronym
