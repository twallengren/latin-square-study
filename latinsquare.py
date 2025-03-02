import random
from typing import List

from permutation import Permutation
from permutationchain import PermutationChain
from transformation import Transformation


class LatinSquare(PermutationChain):
    """
    Represents a Latin square, a special type of permutation chain where the transposed
    version is also a valid permutation chain.
    """

    def __init__(self, permutations: List[Permutation]):
        """
        Initializes a Latin square and validates its structure.

        Args:
            permutations (List[Permutation]): A list of permutations representing rows of a Latin square.

        Raises:
            ValueError: If the given permutations do not form a valid Latin square.
        """
        super().__init__(permutations)
        if Transformation.transpose(self) is None:
            raise ValueError("Invalid Latin Square: Transposed version is not a valid permutation chain.")

    @staticmethod
    def generate(n: int) -> "LatinSquare":
        """
        Generates a random Latin square of size n x n.

        Args:
            n (int): The size of the Latin square.

        Returns:
            LatinSquare: A randomly generated Latin square.
        """
        base = list(range(n))
        permutations = [Permutation(random.sample(base, len(base))) for _ in range(n)]

        # Ensure it is a Latin square by regenerating until valid
        while Transformation.transpose(PermutationChain(permutations)) is None:
            permutations = [Permutation(random.sample(base, len(base))) for _ in range(n)]

        return LatinSquare(permutations)