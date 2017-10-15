"""Test the newton function."""
import newton


def test_newton_normal():
    """Test function under normal conditions."""
    assert newton.square_root_with_newton_method(4, 1) == 2.000


def test_newton_number_zero():
    """Test function if number is 0."""
    assert newton.square_root_with_newton_method(0, 1) is None


def test_newton_iterations_zero():
    """Test function if iterations is 0."""
    assert newton.square_root_with_newton_method(16, 0) == 8.000


def test_newton_number_negative():
    """Test function if number is negative."""
    assert newton.square_root_with_newton_method(-1, 20) is None


def test_newton_iterations_negative():
    """Test function if iterations is negative."""
    assert newton.square_root_with_newton_method(20, -1) is None


def test_newton_decimal_points():
    """Check if the returned value has a maximum of 3 decimal points."""
    assert newton.square_root_with_newton_method(401, 10) == 20.025


def test_newton__points():
    """Check if the returned value has a maximum of 3 decimal points."""
    assert newton.square_root_with_newton_method(16, 1.5) == 5.000


def test_newton_high_iterations():
    assert newton.square_root_with_newton_method(20, 1000) == 4.472
