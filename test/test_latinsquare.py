import unittest
from permutation import Permutation
from latinsquare import LatinSquare  # Assuming this is the module where LatinSquare is defined


class TestLatinSquare(unittest.TestCase):

    def test_valid_latin_square_initialization(self):
        """Test that a valid Latin square initializes correctly."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        p3 = Permutation([2, 0, 1])
        latin_square = LatinSquare([p1, p2, p3])
        self.assertEqual(len(latin_square), 3)

    def test_invalid_latin_square_raises_error(self):
        """Test that an invalid Latin square raises a ValueError."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        p3 = Permutation([1, 2, 0])  # Not a valid Latin square (duplicate column values)

        with self.assertRaises(ValueError):
            LatinSquare([p1, p2, p3])

    def test_generate_latin_square(self):
        """Test that the generate method produces a valid Latin square."""
        latin_square = LatinSquare.generate(4)
        self.assertEqual(len(latin_square), 4)  # Ensure correct dimensions
        self.assertIsInstance(latin_square, LatinSquare)  # Ensure instance is a LatinSquare


if __name__ == "__main__":
    unittest.main()
