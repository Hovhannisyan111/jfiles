# test_calculator.py

from calculator import add, subtract

def test_add():
    """Test the add function."""
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
    assert subtract(-2, -1) == -1
