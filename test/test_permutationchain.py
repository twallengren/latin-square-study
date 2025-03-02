import unittest
from permutation import Permutation
from permutationchain import PermutationChain  # Assuming it's in a separate file

class TestPermutationChain(unittest.TestCase):

    def test_to_array(self):
        """Test conversion to a list of lists."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        chain = PermutationChain([p1, p2])
        expected_array = [[0, 1, 2], [2, 0, 1]]
        self.assertEqual(chain.to_array(), expected_array)

    def test_to_tuple(self):
        """Test conversion to a tuple format for hashing."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        chain = PermutationChain([p1, p2])
        expected_tuple = ((0, 1, 2), (2, 0, 1))
        self.assertEqual(chain.to_tuple(), expected_tuple)

    def test_equality(self):
        """Test that two identical permutation chains are considered equal."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        chain1 = PermutationChain([p1, p2])
        chain2 = PermutationChain([p1, p2])
        self.assertEqual(chain1, chain2)

    def test_inequality(self):
        """Test that different permutation chains are not considered equal."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])  # Different permutation
        chain1 = PermutationChain([p1, p2])
        chain2 = PermutationChain([p1, p3])
        self.assertNotEqual(chain1, chain2)

    def test_hashing(self):
        """Test that identical permutation chains have the same hash value."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        chain1 = PermutationChain([p1, p2])
        chain2 = PermutationChain([p1, p2])
        self.assertEqual(hash(chain1), hash(chain2))

    def test_getitem(self):
        """Test accessing elements of the permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        chain = PermutationChain([p1, p2])
        self.assertEqual(chain[0], p1)
        self.assertEqual(chain[1], p2)

    def test_len(self):
        """Test the length of the permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        chain = PermutationChain([p1, p2])
        self.assertEqual(len(chain), 2)

if __name__ == "__main__":
    unittest.main()
