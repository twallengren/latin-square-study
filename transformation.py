from typing import Optional, List

from permutation import Permutation
from permutationchain import PermutationChain


class Transformation:
    """
    Provides symmetry transformations for permutation chains.
    """

    @staticmethod
    def permute_rows(chain: "PermutationChain", perm: Permutation) -> "PermutationChain":
        """
        Applies a row permutation to the permutation chain.

        Args:
            chain (PermutationChain): The input permutation chain.
            perm (Permutation): The row permutation to apply.

        Returns:
            PermutationChain: A new permutation chain with the specified row permutation applied.
        """
        new_chain: List[Optional[Permutation]] = [None for _ in range(len(chain))]
        for current_index, desired_index in enumerate(perm.values):
            new_chain[desired_index] = chain[current_index]

        return PermutationChain(new_chain)

    @staticmethod
    def permute_columns(chain: "PermutationChain", perm: Permutation) -> "PermutationChain":
        """
        Applies a column permutation to the permutation chain.

        Args:
            chain (PermutationChain): The input permutation chain.
            perm (Permutation): The column permutation to apply.

        Returns:
            PermutationChain: A new permutation chain with the specified column permutation applied.
        """
        new_permutations = []

        for row in chain:
            permuted_values = row.values[:]  # Copy row values
            for old_index, new_index in enumerate(perm.values):
                permuted_values[new_index] = row.values[old_index]
            new_permutations.append(Permutation(permuted_values))

        return PermutationChain(new_permutations)

    @staticmethod
    def transpose(chain: "PermutationChain") -> Optional["PermutationChain"]:
        """
        Transposes a square permutation chain if valid.

        Args:
            chain (PermutationChain): The input permutation chain.

        Returns:
            Optional[PermutationChain]: The transposed chain if valid, otherwise None.
        """
        n = len(chain)
        if any(len(p.values) != n for p in chain.permutations):
            return None  # Not a square matrix
        transposed = [[chain.permutations[j].values[i] for j in range(n)] for i in range(n)]
        try:
            return PermutationChain([Permutation(row) for row in transposed])
        except ValueError:
            return None  # Invalid permutation chain after transpose

    @staticmethod
    def rotate(chain: "PermutationChain", direction: str, rotations: int) -> Optional["PermutationChain"]:
        """
        Rotates a square permutation chain by 90-degree increments.

        Args:
            chain (PermutationChain): The input permutation chain.
            direction (str): "clockwise" or "counterclockwise".
            rotations (int): Number of 90-degree rotations.

        Returns:
            Optional[PermutationChain]: The rotated chain if valid, otherwise None.
        """
        n = len(chain)
        if any(len(p.values) != n for p in chain.permutations):
            return None  # Not a square matrix

        rotated = [row.values[:] for row in chain.permutations]
        for _ in range(rotations % 4):
            if direction == "clockwise":
                rotated = [[rotated[n - j - 1][i] for j in range(n)] for i in range(n)]
            else:
                rotated = [[rotated[j][n - i - 1] for j in range(n)] for i in range(n)]

        try:
            return PermutationChain([Permutation(row) for row in rotated])
        except ValueError:
            return None  # Invalid permutation chain after rotation