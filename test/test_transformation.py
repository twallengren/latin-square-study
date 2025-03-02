import unittest
from permutation import Permutation
from permutationchain import PermutationChain
from transformation import Transformation


class TestTransformation(unittest.TestCase):

    def test_swap_rows(self):
        """Test swapping rows in a permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])

        swapped_chain = Transformation.swap_rows(chain, 0, 2)
        expected = PermutationChain([p3, p2, p1])
        self.assertEqual(swapped_chain, expected)

    def test_swap_columns(self):
        """Test swapping columns in a permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])

        swapped_chain = Transformation.swap_columns(chain, 0, 2)
        expected = PermutationChain([Permutation([2, 1, 0]),
                                     Permutation([1, 0, 2]),
                                     Permutation([0, 2, 1])])
        self.assertEqual(swapped_chain, expected)

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
