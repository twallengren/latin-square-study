import unittest

from differenceoperator import DifferenceOperator
from permutation import Permutation
from permutationchain import PermutationChain


class TestDifferenceOperator(unittest.TestCase):

    def test_difference(self):
        """Test computing the difference between two permutations."""
        p1 = Permutation([2, 0, 1])
        p2 = Permutation([1, 2, 0])
        result = DifferenceOperator.difference(p1, p2)
        self.assertEqual(result.to_tuple(), (1, 2, 0))

    def test_derivative(self):
        """Test computing the derivative of a permutation chain."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])
        derivative_chain = DifferenceOperator.derivative(chain)
        expected = PermutationChain([
            Permutation([1, 2, 0]),
            Permutation([1, 2, 0]),
            Permutation([1, 2, 0])
        ])
        self.assertEqual(derivative_chain, expected)

    def test_order(self):
        """Test computing the order of a permutation chain under repeated application of the derivative."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([2, 0, 1])
        p3 = Permutation([1, 2, 0])
        chain = PermutationChain([p1, p2, p3])
        order = DifferenceOperator.order(chain)
        self.assertEqual(order, 2)  # Ensuring a valid cycle length

    def test_identity_order(self):
        """Test that an identity permutation chain has order 1."""
        p1 = Permutation([0, 1, 2])
        p2 = Permutation([0, 1, 2])
        p3 = Permutation([0, 1, 2])
        identity_chain = PermutationChain([p1, p2, p3])
        self.assertEqual(DifferenceOperator.order(identity_chain), 0)

    def test_empty_chain(self):
        """Test that an empty permutation chain returns -1 for order."""
        empty_chain = PermutationChain([])
        self.assertEqual(DifferenceOperator.order(empty_chain), -1)

if __name__ == "__main__":
    unittest.main()
