import unittest
from permutation import Permutation  # Assuming the class is saved in permutation.py


class TestPermutation(unittest.TestCase):

    def test_valid_permutation(self):
        """Test that valid permutations are correctly initialized."""
        p = Permutation([2, 0, 1])
        self.assertEqual(p.to_tuple(), (2, 0, 1))

    def test_invalid_permutation(self):
        """Test that an invalid permutation raises a ValueError."""
        with self.assertRaises(ValueError):
            Permutation([0, 1, 1])  # Duplicate value

        with self.assertRaises(ValueError):
            Permutation([0, 2, 3])  # Missing a value

        with self.assertRaises(ValueError):
            Permutation([0, 1, 2, 3, 5])  # Out-of-range value

    def test_inverse(self):
        """Test computing the inverse of a permutation."""
        p = Permutation([2, 0, 1])
        inverse_p = p.inverse()
        self.assertEqual(inverse_p.to_tuple(), (1, 2, 0))

    def test_apply_permutation(self):
        """Test applying one permutation to another."""
        p1 = Permutation([2, 0, 1])
        p2 = Permutation([1, 2, 0])
        result = p1.apply(p2)
        self.assertEqual(result.to_tuple(), (0, 1, 2))  # (2,0,1) applied to (1,2,0)

    def test_hashing(self):
        """Test that permutations can be used as dictionary keys."""
        p1 = Permutation([2, 0, 1])
        p2 = Permutation([1, 2, 0])
        d = {p1: "first", p2: "second"}
        self.assertEqual(d[p1], "first")
        self.assertEqual(d[p2], "second")


if __name__ == "__main__":
    unittest.main()
