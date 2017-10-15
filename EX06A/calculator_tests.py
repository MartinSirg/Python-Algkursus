"""Calculator Tester."""
import calculator


def test_repeat_zero_length():
    """Test repeat function when length is 0."""
    assert calculator.repeat("string", 0) == ""


def test_repeat_negative_length():
    """Test repeat function when length is a negative number."""
    assert calculator.repeat("string", -2) == ""


def test_repeat_abc_2():
    """Test repeat function when the string is abc."""
    assert calculator.repeat("abc", 2) == "abcabc"


def test_repeat_empty():
    """Test repeat function when the string is empty."""
    assert calculator.repeat("", 2) == ""


def test_convert_name_two():
    """Test the convert_name function when the string is less than 3 chars long."""
    assert calculator.convert_name("tw") == "ERROR"


def test_convert_name_short():
    """Test the convert_name function when the string is the shortest length(3)."""
    assert calculator.convert_name("two") == "TWO-3wo"


def test_convert_name_no_lower_at_end():
    """Make sure that the last two chars are lower case when returned."""
    assert calculator.convert_name("EXAMPLE") == "EXA-7le"


def test_convert_name_no_upper_in_beginning():
    """Make sure that the first three chars are upper case when returned."""
    assert calculator.convert_name("calculator") == "CAL-10or"


def test_addition():
    """Test the addition function under normal conditions."""
    assert calculator.addition(1, 2) == "1 + 2 = 3"


def test_addition_neg():
    """Test the addition function when both arguments are negative."""
    assert calculator.addition(-1, -2) == "-1 + -2 = -3"


def test_addition_neg_a():
    """Test the addition function when the first argument is a negative number."""
    assert calculator.addition(-1, 2) == "-1 + 2 = 1"


def test_addition_neg_b():
    """Test the addition function when the second argument is a negative number."""
    assert calculator.addition(1, -2) == "1 + -2 = -1"


def test_subtraction():
    """Test the subtraction function under normal conditions."""
    assert calculator.subtraction(1, 2) == "1 - 2 = -1"


def test_subtraction_neg():
    """TTest the subtraction function when both arguments are negative."""
    assert calculator.subtraction(-1, -2) == "-1 - -2 = 1"


def test_subtraction_neg_a():
    """Test the subtraction function when the first argument is a negative number."""
    assert calculator.subtraction(-1, 2) == "-1 - 2 = -3"


def test_subtraction_neg_b():
    """Test the subtraction function when the second argument is a negative number."""
    assert calculator.subtraction(1, -2) == "1 - -2 = 3"


def test_line_empty():
    """Make sure the decorated parameter is set to False by default when second parameter is left empty."""
    assert calculator.line(4,) == "----"


def test_line_not_decorated():
    """Test the line function when decorated is set to False."""
    assert calculator.line(4, False) == "----"


def test_line_decorated():
    """Test the line function when decorated is set to True."""
    assert calculator.line(4, True) == ">--<"


def test_line_small_decorated():
    """Make sure when length is less than two and decorated is false, the returned value is ""."""
    assert calculator.line(1, True) == ""


def test_line_small_not_decorated():
    """Make sure that when length is the shortest(1) and decorated is set to false, the returned value is not ""."""
    assert calculator.line(1, False) == "-"


def test_display_addition():
    """Test the display function when addition is used."""
    assert calculator.display(1, 200, "kekmachine", "addition", ) == "       KEK-10ne\n>-------------<\n\
|1 + 200 = 201|\n---------------"


def test_display_subtraction():
    """Test the display function when subtraction is used."""
    assert calculator.display(200, 1, "kekmachine", "subtraction", ) == "       KEK-10ne\n>-------------<\n\
|200 - 1 = 199|\n---------------"


def test_display_other():
    """Make sure that when the operation parameter is something else than subtraction or addition,\
the returned "ERROR" ."""
    assert calculator.display(200, 1, "kekmachine", "other", ) == "ERROR"
