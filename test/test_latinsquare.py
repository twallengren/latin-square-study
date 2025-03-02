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

    def test_reduce_valid_latin_square(self):
        """Test reducing a Latin square to its canonical form."""
        p1 = Permutation([2, 0, 1])
        p2 = Permutation([0, 1, 2])
        p3 = Permutation([1, 2, 0])
        latin_square = LatinSquare([p1, p2, p3])

        reduced_square = LatinSquare.reduce(latin_square)

        expected = LatinSquare([
            Permutation([0, 1, 2]),  # First row sorted
            Permutation([1, 2, 0]),  # First column sorted
            Permutation([2, 0, 1])
        ])
        self.assertEqual(reduced_square, expected)

    def test_reduce_already_reduced(self):
        """Test that a Latin square that is already in reduced form remains unchanged."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        p3 = Permutation([2, 0, 1])
        latin_square = LatinSquare([p1, p2, p3])

        reduced_square = LatinSquare.reduce(latin_square)

        self.assertEqual(reduced_square, latin_square)  # Should be unchanged

    def test_reduce_first_row_sorted(self):
        """Test that the first row of the reduced Latin square is in ascending order."""
        latin_square = LatinSquare.generate(4)
        reduced_square = LatinSquare.reduce(latin_square)
        first_row = reduced_square.permutations[0].values
        self.assertEqual(first_row, list(range(4)))

    def test_reduce_first_column_sorted(self):
        """Test that the first column of the reduced Latin square is in ascending order."""
        latin_square = LatinSquare.generate(4)
        reduced_square = LatinSquare.reduce(latin_square)
        first_column = [p.values[0] for p in reduced_square.permutations]
        self.assertEqual(first_column, list(range(4)))


if __name__ == "__main__":
    unittest.main()
