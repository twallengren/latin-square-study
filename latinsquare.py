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

    @staticmethod
    def reduce(square: "LatinSquare") -> "LatinSquare":
        """
        Reduces the Latin square by applying column transformations so that
        the first row is in ascending order, then applying row transformations
        so the first column is in ascending order.

        Returns:
            LatinSquare: The reduced form of the Latin square.
        """

        col_permuted = Transformation.permute_columns(square, square.permutations[0])
        first_column = [p.values[0] for p in col_permuted.permutations]
        row_permutation = Permutation(first_column)
        reduced_square = Transformation.permute_rows(col_permuted, row_permutation)

        return LatinSquare(reduced_square.permutations)