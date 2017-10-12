import calculator

def test_repeat_zero_length():
    assert calculator.repeat("string", 0) == ""

def test_repeat_negative_length():
    assert calculator.repeat("string", -2) == ""

def test_repeat_a_5():
    assert calculator.repeat("a", 5) == "aaaaa"

def test_repeat_abc_2():
    assert calculator.repeat("abc", 2) == "abcabc"