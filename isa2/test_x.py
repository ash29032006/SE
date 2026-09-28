"""Unit tests for the calculator module (x.py)."""

import unittest
from x import add, subtract, multiply, divide, factorial


class TestAdd(unittest.TestCase):
    """Tests for the add function."""

    def test_positive_numbers(self):
        """Add two positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        """Add two negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_mixed_sign(self):
        """Add a positive and a negative number."""
        self.assertEqual(add(-1, 1), 0)

    def test_floats(self):
        """Add two floating-point numbers."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract function."""

    def test_positive_result(self):
        """Subtract to get a positive result."""
        self.assertEqual(subtract(10, 3), 7)

    def test_negative_result(self):
        """Subtract to get a negative result."""
        self.assertEqual(subtract(3, 10), -7)

    def test_zero_result(self):
        """Subtract equal numbers to get zero."""
        self.assertEqual(subtract(5, 5), 0)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply function."""

    def test_positive_numbers(self):
        """Multiply two positive numbers."""
        self.assertEqual(multiply(4, 5), 20)

    def test_by_zero(self):
        """Multiply by zero."""
        self.assertEqual(multiply(100, 0), 0)

    def test_negative_numbers(self):
        """Multiply two negatives gives positive."""
        self.assertEqual(multiply(-3, -2), 6)


class TestDivide(unittest.TestCase):
    """Tests for the divide function."""

    def test_even_division(self):
        """Divide evenly."""
        self.assertEqual(divide(10, 2), 5)

    def test_float_division(self):
        """Divide with a float result."""
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(1, 0)


class TestFactorial(unittest.TestCase):
    """Tests for the factorial function."""

    def test_zero(self):
        """Factorial of 0 is 1."""
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        """Factorial of 5 is 120."""
        self.assertEqual(factorial(5), 120)

    def test_one(self):
        """Factorial of 1 is 1."""
        self.assertEqual(factorial(1), 1)

    def test_negative_raises(self):
        """Negative input raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer_raises(self):
        """Non-integer input raises TypeError."""
        with self.assertRaises(TypeError):
            factorial(3.5)


if __name__ == "__main__":
    unittest.main()
