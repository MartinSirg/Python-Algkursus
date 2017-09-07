""""Calculator."""
import math


def value_of_z(ex, x, y):
    """Write a function which calculates the value of z."""

    if ex == 1:
        return (x ** y) + (y ** x)
    elif ex == 2:
        return (x / 5.6) - (y / 6.5)
    elif ex == 3:
        return (x * y ** 4 * math.log(5) / 5) / (1 + (7 * math.sqrt(x**2 + y**2)))
    else:
        print("Sellist ülesannet ei ole!")
        return None
