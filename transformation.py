from typing import Optional

from permutation import Permutation
from permutationchain import PermutationChain


class Transformation:
    """
    Provides symmetry transformations for permutation chains.
    """

    @staticmethod
    def swap_rows(chain: "PermutationChain", i: int, j: int) -> "PermutationChain":
        """
        Swaps two rows in a permutation chain.

        Args:
            chain (PermutationChain): The input permutation chain.
            i (int): Index of the first row to swap.
            j (int): Index of the second row to swap.

        Returns:
            PermutationChain: A new permutation chain with the specified rows swapped.
        """
        swapped = chain.permutations[:]
        swapped[i], swapped[j] = swapped[j], swapped[i]
        return PermutationChain(swapped)

    @staticmethod
    def swap_columns(chain: "PermutationChain", i: int, j: int) -> "PermutationChain":
        """
        Swaps two columns in a permutation chain.

        Args:
            chain (PermutationChain): The input permutation chain.
            i (int): Index of the first column to swap.
            j (int): Index of the second column to swap.

        Returns:
            PermutationChain: A new permutation chain with the specified columns swapped.
        """
        swapped = [Permutation(p.values[:]) for p in chain.permutations]
        for row in swapped:
            row.values[i], row.values[j] = row.values[j], row.values[i]
        return PermutationChain(swapped)

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