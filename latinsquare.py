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
    def generate_random(n: int) -> "LatinSquare":
        """
        Generates a random Latin square of size n x n using a column map.
        Retries if an unsolvable configuration is encountered.

        Args:
            n (int): The size of the Latin square.

        Returns:
            LatinSquare: A randomly generated Latin square.
        """
        while True:  # Keep retrying until we succeed
            try:
                # Step 1: Generate a random first row
                first_row = list(range(n))
                random.shuffle(first_row)

                # Step 2: Initialize column tracking
                column_map = {val: {i} for i, val in enumerate(first_row)}  # Tracks column positions of each number
                permutations = [Permutation(first_row)]  # Store first row

                # Step 3: Generate remaining rows
                for _ in range(n - 1):
                    row = [-1] * n  # Placeholder row
                    available_columns = {val: set(range(n)) - column_map[val] for val in
                                         range(n)}  # Track valid columns

                    numbers_to_place = set(range(n))  # All numbers need placement
                    while numbers_to_place:
                        # Step 3.1: Select the most constrained value first (fewest available columns)
                        value = min(numbers_to_place, key=lambda v: len(available_columns[v]))
                        possible_columns = list(available_columns[value])  # Allowed columns

                        chosen_column = random.choice(possible_columns)  # Randomly pick a valid column
                        row[chosen_column] = value  # Place number

                        # Update tracking
                        column_map[value].add(chosen_column)
                        for v in available_columns:
                            available_columns[v].discard(chosen_column)  # Remove column from all number options

                        numbers_to_place.remove(value)  # Mark number as placed

                    permutations.append(Permutation(row))

                return LatinSquare(permutations)  # Successfully generated a valid Latin square

            except IndexError:
                # If an error occurs (e.g., no valid column left), restart with a new random first row
                continue

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