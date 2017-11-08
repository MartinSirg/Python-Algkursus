"""Tunnikontroll."""


def count_lower(s):
    """
    count the number of lower ascii letters in the string.

    :param s: string
    :return: int, count of lower ascii letters
    """
    count = 0
    for i in range(len(s)):
        if s[i].islower() is True:
            count += 1
    return count


def ends_with_pair(s):
    """
    if string ends with pair of symbols, return the index of the start of the pair.
    if not, return the index of the last symbol.
    else, return -1

    :param s: string
    :return: int, index of pair or index of single symbol or -1
    """
    if len(s) > 2:
        if s[-1] == s[-2]:
            return len(s) - 2
        else:
            return len(s) - 1
    elif len(s) > 0:
        return s.index(s[-1])
    else:
        return -1


def swap_pos(numbers, pos):
    """
    takes the value of element in position pos. this value is swapped
    with the element in position of the value.

    if cannot swap, change nothing.

    :param numbers: list of ints
    :param pos: int, position
    :return: list of ints
    """
    try:
        nums = numbers
        value = nums[pos]
        second_value = nums[value]
        nums[pos] = second_value
        nums[value] = value
        return nums
    except:
        return numbers


def merge_lists(a, b):
    """
    take first element from a, first element of b, second element of a, second element of b etc.
    if one list ends, then don't continue with the second list.

    :param a: list
    :param b: list
    :return: merged list
    """
    minimum = min(len(a), len(b))
    if minimum == 0:
        return []
    result = []
    for i in range(minimum):
        result.append(a[i])
        result.append(b[i])
    return result


if __name__ == '__main__':
    print(count_lower("tere"))     # => 4
    print(count_lower("tere1"))    # => 4
    print(count_lower("123"))      # => 0
    print(count_lower("AaAa"))     # => 2
    print(count_lower(""))         # => 0
    print("Endwithpair----------------------")

    print(ends_with_pair("tere"))  # => 3
    print(ends_with_pair("aa"))    # => 0
    print(ends_with_pair("ab"))    # => 1
    print(ends_with_pair("a"))     # => 0
    print(ends_with_pair(""))      # => -1
    print("Swap pos-------------------")
    print(swap_pos([1, 2, 3], 0))  # => [2, 1, 3]
    print(swap_pos([1, 2, 3], 1))  # => [1, 3, 2]
    print(swap_pos([1, 2, 3], 2))  # => [1, 2, 3]
    print(swap_pos([1, 2, 3], 3))  # => [1, 2, 3]
    print(swap_pos([1, 4, 6, 2, 5], 3)) # => [1, 4, 2, 6, 5]
    print(swap_pos([], 4)) # => []
    print(swap_pos([1, 1, 1], 0)) # => [1, 1, 1]

    print("MERGE--------------")
    print(merge_lists([1, 2, 3], [1, 2, 3])) # => [1, 1, 2, 2, 3, 3]
    print(merge_lists([1], [2, 3])) # => [1, 2]
    print(merge_lists([], [1, 2, 3])) # => []
    print(merge_lists([], [])) # => []
    print(merge_lists([4, 5, 6, 7], [1])) # => [4, 1]