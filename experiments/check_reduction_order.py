from typing import Dict, Any, List

from differenceoperator import DifferenceOperator
from experiment import Experiment
from latinsquare import LatinSquare

def check_reduction_order(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Checks whether reducing a Latin square preserves its order under D.

    Args:
        params (Dict[str, Any]): Contains 'n' (size of Latin square).

    Returns:
        Dict[str, Any]: A dictionary containing the original and reduced orders.
    """
    n = params["n"]
    latin_square = LatinSquare.generate_random(n)

    original_order = DifferenceOperator.order(latin_square)
    reduced_order = DifferenceOperator.order(LatinSquare.reduce(latin_square))

    return {"n": n, "original_order": original_order, "reduced_order": reduced_order}


def merge_order_classes(order_classes: List[set], new_pair: set) -> List[set]:
    """
    Merges order classes if they overlap with the new pair.

    Args:
        order_classes (List[set]): List of existing order classes.
        new_pair (set): The new set containing original and reduced orders.

    Returns:
        List[set]: Updated order classes with merged sets.
    """
    merged_classes = []
    merged = False

    for order_class in order_classes:
        if order_class & new_pair:  # If there's an intersection, merge
            merged_classes.append(order_class | new_pair)
            merged = True
        else:
            merged_classes.append(order_class)

    if not merged:
        merged_classes.append(new_pair)  # If no merge occurred, add new set

    # Final pass to merge any overlapping sets
    final_classes = []
    while merged_classes:
        current_set = merged_classes.pop()
        merged = False
        for i, existing_set in enumerate(final_classes):
            if existing_set & current_set:
                final_classes[i] = existing_set | current_set
                merged = True
                break
        if not merged:
            final_classes.append(current_set)

    return final_classes


if __name__ == "__main__":
    # Run the experiment
    experiment = Experiment("Reduction Order Test", check_reduction_order)
    experiment.run(params={"n": 7}, num_trials=5000, num_workers=8)

    order_classes = []

    for result in experiment.results:
        original_order = result["original_order"]
        reduced_order = result["reduced_order"]

        new_order_pair = {original_order, reduced_order}
        order_classes = merge_order_classes(order_classes, new_order_pair)

    # Print the final order classes
    print("Final Order Classes:")
    for order_class in order_classes:
        print(sorted(order_class))
