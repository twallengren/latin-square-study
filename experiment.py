from typing import Callable, Dict, Any, List
import pandas as pd
import concurrent.futures
from tqdm import tqdm

class Experiment:
    """
    A framework for running experiments on Latin squares.
    """

    def __init__(self, name: str, func: Callable[[Dict[str, Any]], Any]):
        """
        Initializes an experiment.

        Args:
            name (str): The name of the experiment.
            func (Callable[[Dict[str, Any]], Any]): A function that defines the experiment.
        """
        self.name = name
        self.func = func
        self.results: List[Dict[str, Any]] = []

    def run(self, params: Dict[str, Any], num_trials: int = 100, num_workers: int = None):
        """
        Runs the experiment multiple times in parallel with the given parameters.

        Args:
            params (Dict[str, Any]): The parameters for the experiment.
            num_trials (int): The number of times to repeat the experiment.
            num_workers (int, optional): The number of parallel workers (defaults to system CPU count).
        """
        self.results = []

        print(f"Running {num_trials} trials in parallel...")

        with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
            futures = {executor.submit(self.func, params): i for i in range(num_trials)}

            with tqdm(total=num_trials, desc=self.name, unit="trial") as pbar:
                for future in concurrent.futures.as_completed(futures):
                    try:
                        result = future.result()
                        self.results.append(result)
                    except Exception as e:
                        print(f"Error in trial {futures[future]}: {e}")
                    pbar.update(1)  # Update progress bar

    def analyze_results(self) -> pd.DataFrame:
        """
        Converts results into a Pandas DataFrame for analysis.

        Returns:
            pd.DataFrame: A DataFrame of experiment results.
        """
        return pd.DataFrame(self.results)

    def summary(self):
        """
        Prints summary statistics of the results.
        """
        df = self.analyze_results()
        print(f"Experiment: {self.name}")
        print(df.describe())
