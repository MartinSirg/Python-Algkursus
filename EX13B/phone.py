"""Call me maybe."""


def how_many_calls(n):
    """
    Return the number of calls made during the current minute.

    Arguments:
    n -- the current minute.
    """
    if not isinstance(n, int) or n < 0:
        return None
    elif n == 0:
        return 0
    elif n <= 3:
        return 2 ** (n - 1)
    return how_many_calls(n - 1) + how_many_calls(n - 2) + how_many_calls(n - 3)


def how_many_people(n):
    """
    Return the number of people who know after n minutes has passed.

    Arguments:
    n -- how many minutes has passed.
    """
    print(n)
    if not isinstance(n, int) or n < 0:
        return None
    elif n <= 3:
        return 2 ** n
    return how_many_people(n - 1) + how_many_calls(n)
