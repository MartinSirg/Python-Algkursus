import calculator


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


def test_addition_neg_a():
    assert calculator.addition(-1, 2) == "-1 + 2 = 1"


def test_addition_neg_b():
    assert calculator.addition(1, -2) == "1 + -2 = -1"


def test_subtraction():
    assert calculator.subtraction(1, 2) == "1 - 2 = -1"


def test_subtraction_neg():
    assert calculator.subtraction(-1, -2) == "-1 - -2 = 1"


def test_subtraction_neg_a():
    assert calculator.subtraction(-1, 2) == "-1 - 2 = -3"


def test_subtraction_neg_b():
    assert calculator.subtraction(1, -2) == "1 - -2 = 3"


def test_line_empty_decorated():
    assert calculator.line(1, True) == ""


def test_line_not_decorated():
    assert calculator.line(4, False) == "----"


def test_line_decorated():
    assert calculator.line(4, True) == ">--<"


def test_line_small_decorated():
    assert calculator.line(1, True) == ""


def test_line_small_not_decorated():
    assert calculator.line(1, False) == "-"


def test_display_addition():
    assert calculator.display(1, 200, "kekmachine", "addition", ) == "       KEK-10ne\n>-------------<\n\
|1 + 200 = 201|\n---------------"

def test_display_subtraction():
    assert calculator.display(200, 1, "kekmachine", "subtraction", ) == "       KEK-10ne\n>-------------<\n\
|200 - 1 = 199|\n---------------"


def test_display_other():
    assert calculator.display(200, 1, "kekmachine", "other", ) == "ERROR"

