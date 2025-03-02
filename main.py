from permutation import Permutation
from permutationchain import PermutationChain
from differenceoperator import DifferenceOperator

def main():
    # Example Latin Squares
    latin_square_4x4 = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    latin_square_5x5 = [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 0],
        [2, 3, 4, 0, 1],
        [3, 4, 0, 1, 2],
        [4, 0, 1, 2, 3]
    ]

    # Compute orders
    chain_4x4 = PermutationChain([Permutation(p) for p in latin_square_4x4])
    chain_5x5 = PermutationChain([Permutation(p) for p in latin_square_5x5])

    order_4x4 = DifferenceOperator.order(chain_4x4)
    order_5x5 = DifferenceOperator.order(chain_5x5)

    print(f"Order of 4x4 Latin Square under D: {order_4x4}")
    print(f"Order of 5x5 Latin Square under D: {order_5x5}")

if __name__ == "__main__":
    main()