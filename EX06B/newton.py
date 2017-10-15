"""Calculate square root with Newton method."""


def square_root_with_newton_method(number, iterations):
    """
    Calculate the given number's approximate square root.

    :param number: number from which the square root will be calculated.
    :param iterations: number of formula cycles, highest integer not bigger than the value (1.9 => 1).
    :return: approximate square root. In the case of non-positive number or negative iterations, return None.
    """
    g = number/2                        # Inital value of g.
    x = number
    if x < 1 or iterations < 0:
        return None
    else:
        for i in range(int(iterations)):    # Cycle based on the iterations number.
            g = (g + x / g) / 2             # Formula in the cycle.
    return round(g, 3)                       # Return the rounded final result.


if __name__ == '__main__':
    print(square_root_with_newton_method(20, 1000))
