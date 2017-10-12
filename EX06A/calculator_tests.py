import calculator
import pytest
def test_repeat_zero_length():
    assert calculator.repeat("string", 0) == ""


def test_repeat_negative_length():
    assert calculator.repeat("string", -2) == ""


def test_repeat_abc_2():
    assert calculator.repeat("abc", 2) == "abcabc"


def test_repeat_empty():
    assert calculator.repeat("", 2) == ""


def test_convert_name_two():
    assert calculator.convert_name("tw") == "ERROR"


def test_convert_name_short():
    assert calculator.convert_name("two") == "TWO-3wo"


def test_convert_name_no_lower_at_end():
    assert calculator.convert_name("EXAMPLE") == "EXA-7le"


def test_convert_name_no_upper_in_beginning():
    assert calculator.convert_name("calculator") == "CAL-10or"


def test_addition():
    assert calculator.addition(1, 2) == "1 + 2 = 3"


def test_addition_neg():
    assert calculator.addition(-1, -2) == "-1 + -2 = -3"

def test_addition_neg():
    assert calculator.addition(-1, 2) == "-1 + 2 = 1"


def test_addition_neg():
    assert calculator.addition(1, -2) == "1 + -2 = -1"