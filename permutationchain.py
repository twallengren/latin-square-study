from typing import List, Tuple

from permutation import Permutation


class PermutationChain:
    """
    Represents a sequence of permutations.
    Provides methods for transformation and hashing.
    """

    def __init__(self, permutations: List[Permutation]):
        """
        Initializes a permutation chain with a list of permutations.

        Args:
            permutations (List[Permutation]): A list of permutations.
        """
        self.permutations = permutations

    def __getitem__(self, index: int) -> Permutation:
        return self.permutations[index]

    def __len__(self) -> int:
        return len(self.permutations)

    def to_array(self) -> List[List[int]]:
        """
        Converts the permutation chain to a list of lists representation.

        Returns:
            List[List[int]]: A list of lists representation of the permutation chain.
        """
        return [p.values for p in self.permutations]

    def to_tuple(self) -> Tuple[Tuple[int, ...], ...]:
        """
        Converts the permutation chain to a tuple format for hashing.

        Returns:
            Tuple[Tuple[int, ...], ...]: A tuple representation of the permutation chain.
        """
        return tuple(p.to_tuple() for p in self.permutations)

    def __repr__(self) -> str:
        return "\n".join(map(str, self.permutations))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PermutationChain):
            return False
        return self.to_tuple() == other.to_tuple()

    def __hash__(self) -> int:
        return hash(self.to_tuple())
