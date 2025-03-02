from typing import List, Tuple


class Permutation:
    """
    Represents a permutation of elements. Provides functionality for computing
    the inverse of a permutation, applying one permutation to another, and converting
    the permutation to a hashable format.
    """

    def __init__(self, values: List[int]):
        """
        Initializes a permutation with the given values and validates its correctness.

        Args:
            values (List[int]): A list representing a permutation.

        Raises:
            ValueError: If the input is not a valid permutation.
        """
        if not self._is_valid_permutation(values):
            raise ValueError("Invalid permutation: Must contain each integer from 0 to N-1 exactly once.")
        self.values = values

    @staticmethod
    def _is_valid_permutation(values: List[int]) -> bool:
        """
        Validates whether the given list is a proper permutation.

        Args:
            values (List[int]): The list to validate.

        Returns:
            bool: True if the list is a valid permutation, False otherwise.
        """
        n = len(values)
        return sorted(values) == list(range(n))

    def inverse(self) -> "Permutation":
        """
        Computes the inverse of the permutation.

        Returns:
            Permutation: The inverse permutation.
        """
        inverse_values = [0] * len(self.values)
        for i, v in enumerate(self.values):
            inverse_values[v] = i
        return Permutation(inverse_values)

    def apply(self, perm: "Permutation") -> "Permutation":
        """
        Applies another permutation to this permutation.

        Args:
            perm (Permutation): Another permutation to apply.

        Returns:
            Permutation: The result of applying `perm` to `self`.
        """
        return Permutation([self.values[i] for i in perm.values])

    def to_tuple(self) -> Tuple[int, ...]:
        """
        Converts the permutation to a tuple format for hashing.

        Returns:
            Tuple[int, ...]: A tuple representation of the permutation.
        """
        return tuple(self.values)

    def __repr__(self) -> str:
        """
        Returns a string representation of the permutation.
        """
        return str(self.values)