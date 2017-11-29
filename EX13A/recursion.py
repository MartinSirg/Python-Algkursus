"""Recursion vs loops."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    :param s: input string
    :return: reversed input string
    """
    new = ""
    for i in range(len(s) - 1, -1, -1):
        new += s[i]
    return new

def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    :param s: input string
    :return: reversed input string
    """
    if len(s) > 0:
        last_char = s[-1]
        next_last = recursive_reverse(s[:-1])
        return last_char + next_last
    return ""

def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    :param n: the last number to add to the sum
    :return: sum
    """
    result = 0
    for i in range(n + 1):
        result += i
    return result

def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    :param n: the last number to add to the sum
    :return: sum
    """
    if n > 0:
        result = n + recursive_sum(n - 1)
        return result
    return 0
