from permutation import Permutation
from permutationchain import PermutationChain


class DifferenceOperator:
    """
    Provides methods to compute the difference between permutations and
    derive the transformation behavior of permutation chains under iteration.
    """

    @staticmethod
    def difference(p1: Permutation, p2: Permutation) -> Permutation:
        """
        Computes the difference between two permutations.

        Args:
            p1 (Permutation): The first permutation.
            p2 (Permutation): The second permutation.

        Returns:
            Permutation: The resulting permutation difference.
        """
        return p2.inverse().apply(p1)

    @staticmethod
    def derivative(chain: PermutationChain) -> PermutationChain:
        """
        Computes the derivative of a permutation chain.

        Args:
            chain (PermutationChain): The input permutation chain.

        Returns:
            PermutationChain: The resulting derivative chain.
        """
        if len(chain) == 0:
            return PermutationChain([])
        return PermutationChain([
            DifferenceOperator.difference(chain[i], chain[(i + 1) % len(chain)])
            for i in range(len(chain))
        ])

    @staticmethod
    def order(chain: PermutationChain) -> int:
        """
        Computes the order of a permutation chain under repeated application of the derivative.

        Args:
            chain (PermutationChain): The input permutation chain.

        Returns:
            int: The number of steps before the chain returns to the identity.
        """
        if len(chain) == 0:
            print("Error: Empty permutation chain received.")
            return -1

        seen = {}
        current = chain
        steps = 0
        identity = PermutationChain([Permutation(list(range(len(chain[0].values)))) for _ in range(len(chain))])

        while True:
            if current in seen:
                cycle_length = steps - seen[current]
                return cycle_length
            seen[current] = steps
            if current == identity:
                return steps
            current = DifferenceOperator.derivative(current)
            steps += 1