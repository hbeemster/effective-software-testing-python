"""This is a more Pythonic implementation."""
from typing import List

from src.effective_software_testing_python.ch01.alternative.estimate import Estimate


def identify_extremes(estimates: List[Estimate]) -> List[str]:
    if estimates is None:
        raise ValueError("Estimates can't be None")

    if len(estimates) <= 1:
        raise ValueError("There has to be more than 1 estimate in the list")

    sorted_estimates = sorted(estimates)

    if sorted_estimates[0] == sorted_estimates[-1]:
        return []

    return [sorted_estimates[0].developer, sorted_estimates[-1].developer]
