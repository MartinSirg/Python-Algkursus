"""I LOVE MATH."""
import math


def get_lines(initial_line_length: float):
    """"Quadratic equation, solve for y.

    x is given as initial_line_length
    y has to be shorter than x-y
    :return y and x-y as tuple
    """
    x = initial_line_length     # y^2 - 3xy + x^2
    b = 3 * x
    c = x ** 2
    y1 = round((b + math.sqrt(b**2 - 4 * c)) / 2)
    y2 = round((b - math.sqrt(b**2 - 4 * c)) / 2)
    if y1 <= int(x - y1):
        return y1, x - y1
    else:
        return y2, x - y2


def finder(row, col):
    """Find table cell value."""
    diagonal_nr = col + row - 1
    count = 0
    for i in range(1, diagonal_nr):
        count += i
    count += row
    return count


def clocky(hour, minute):
    """
    Calculate the angle between the hour and minute pointer.

    :param hour: has to be between 1 and 12 inclusive
    :param minute: has to be between 0 and 59 inclusive
    :return: angle
    """
    if hour > 12 or hour < 1 or minute > 59 or minute < 0:
        return -1
    if hour == 12:
        hour = 0
    else:
        hour = hour * 30
    minute = minute * 6
    if hour - minute < 0:
        return minute - hour
    return hour - minute
