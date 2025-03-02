import unittest
from permutation import Permutation
from permutationchain import PermutationChain
from transformation import Transformation


class TestTransformation(unittest.TestCase):

    def test_permute_rows(self):
        """Test applying a row permutation to a permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])

        row_permutation = Permutation([2, 0, 1])  # Move row 0 → 2, row 1 → 0, row 2 → 1
        permuted_chain = Transformation.permute_rows(chain, row_permutation)

        expected = PermutationChain([p3, p1, p2])  # Reordered accordingly
        self.assertEqual(permuted_chain, expected)

    def test_permute_columns(self):
        """Test applying a column permutation to a permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])

        column_permutation = Permutation([2, 0, 1])  # Move col 0 → 2, col 1 → 0, col 2 → 1
        permuted_chain = Transformation.permute_columns(chain, column_permutation)

        expected = PermutationChain([
            Permutation([1, 2, 0]),  # New column order for p1
            Permutation([0, 1, 2]),  # New column order for p2
            Permutation([2, 0, 1])   # New column order for p3
        ])
        self.assertEqual(permuted_chain, expected)

    def test_transpose_valid(self):
        """Test transposing a valid square permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])

        transposed_chain = Transformation.transpose(chain)
        expected = PermutationChain([Permutation([0, 2, 1]),
                                     Permutation([1, 0, 2]),
                                     Permutation([2, 1, 0])])
        self.assertEqual(transposed_chain, expected)

    def test_transpose_invalid_not_permutation(self):
        """Test transposing a valid square permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([0, 1, 2])
        p3 = Permutation([0, 1, 2])
        chain = PermutationChain([p1, p2, p3])

        transposed_chain = Transformation.transpose(chain)
        self.assertIsNone(transposed_chain)

    def test_transpose_invalid_not_square(self):
        """Test transposing an invalid non-square permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2])  # Not square

        transposed_chain = Transformation.transpose(chain)
        self.assertIsNone(transposed_chain)

    def test_rotate_clockwise(self):
        """Test rotating a square permutation chain clockwise."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        p3 = Permutation([2, 0, 1])
        chain = PermutationChain([p1, p2, p3])

        rotated_chain = Transformation.rotate(chain, "clockwise", 1)
        expected = PermutationChain([Permutation([2, 1, 0]),
                                     Permutation([0, 2, 1]),
                                     Permutation([1, 0, 2])])
        self.assertEqual(rotated_chain, expected)

    def test_rotate_counterclockwise(self):
        """Test rotating a square permutation chain counterclockwise."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        p3 = Permutation([2, 0, 1])
        chain = PermutationChain([p1, p2, p3])

        rotated_chain = Transformation.rotate(chain, "counterclockwise", 1)
        expected = PermutationChain([Permutation([2, 0, 1]),
                                     Permutation([1, 2, 0]),
                                     Permutation([0, 1, 2])])
        self.assertEqual(rotated_chain, expected)

    def test_rotate_invalid_not_permutation(self):
        """Test transposing a valid square permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([0, 1, 2])
        p3 = Permutation([0, 1, 2])
        chain = PermutationChain([p1, p2, p3])

        transposed_chain = Transformation.rotate(chain, "clockwise", 1)
        self.assertIsNone(transposed_chain)

    def test_rotate_invalid(self):
        """Test rotating an invalid non-square permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2])  # Not square

        rotated_chain = Transformation.rotate(chain, "clockwise", 1)
        self.assertIsNone(rotated_chain)


if __name__ == "__main__":
    unittest.main()
