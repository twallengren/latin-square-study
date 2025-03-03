from typing import Dict, Any

from differenceoperator import DifferenceOperator
from experiment import Experiment
from latinsquare import LatinSquare


def analyze_order_vs_reduced_form(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyzes whether squares with the same order have the same reduced form.

    Args:
        params (Dict[str, Any]): Contains 'n' (size of Latin square).

    Returns:
        Dict[str, Any]: Contains order, reduced form hash.
    """
    n = params["n"]
    latin_square = LatinSquare.generate_random(n)

    order = DifferenceOperator.order(latin_square)
    reduced = LatinSquare.reduce(latin_square)

    return {"n": n, "order": order, "reduced": reduced}

if __name__ == "__main__":
    experiment = Experiment("Order vs. Reduced Form", analyze_order_vs_reduced_form)
    experiment.run(params={"n": 5}, num_trials=10000, num_workers=8)

    # Group by order and compare reduced forms
    results = experiment.results
    reduced_forms = set()
    for result in results:
        order = result["order"]
        reduced_form = result["reduced"]
        reduced_forms.add(reduced_form)

    print(f"Unique reduced forms: {len(reduced_forms)}")
    for reduced_form in reduced_forms:

        order = DifferenceOperator.order(reduced_form)

        print("************************")
        print(f"Order: {order}")
        print(reduced_form)
