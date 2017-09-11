""""Comparator."""


def comparator(num: float) -> str:
    """
    Compare the given number with 5 and return message depending on the number's value.

    :param num: input number
    :return: message regarding the number value compared to five.
    """
    if num < 5:
        return "The input number is smaller than 5!"
    elif num > 5:
        return "The input number is bigger than 5!"
    else:
        return "The input number is 5!"
