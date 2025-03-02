import numpy as np

from permutation import Permutation
from permutationchain import PermutationChain

class DifferenceOperator:
    @staticmethod
    def difference(p1, p2):
        return p2.inverse().apply(p1)

    @staticmethod
    def derivative(chain):
        if len(chain) == 0:
            return PermutationChain([])
        return PermutationChain([
            DifferenceOperator.difference(chain[i], chain[(i + 1) % len(chain)])
            for i in range(len(chain))
        ])

    @staticmethod
    def order(chain):
        if len(chain) == 0:
            print("Error: Empty permutation chain received.")
            return -1  # Indicate an error

        seen = {}
        current = chain
        steps = 0
        identity = PermutationChain([Permutation(np.arange(len(chain[0].values))) for _ in range(len(chain))])

        while True:
            print(f"Step {steps}:\n{current}")  # Debugging output
            if current in seen:
                cycle_length = steps - seen[current]
                print(f"Cycle detected at step {steps}, true order is {cycle_length}")
                return cycle_length
            seen[current] = steps
            if current == identity:
                print(f"Reached identity at step {steps}.")
                return steps
            current = DifferenceOperator.derivative(current)
            steps += 1