"""Module with the PlanningPoker class."""
from typing import List

from src.effective_software_testing_python.ch01.ch01_book.esitmate import Estimate


class PlanningPoker:
    """PlanningPoker class."""

    # ------------------------------------------------------------------------
    @staticmethod
    def identify_extremes(estimates: List[Estimate]) -> List[str]:
        """Returns the extremes of the given estimates."""

        if estimates is None:
            raise ValueError("Estimates can't be None")

        if len(estimates) <= 1:
            raise ValueError("There has to be more than 1 estimate in the list")

        lowest_estimate = None
        highest_estimate = None

        for estimate in estimates:
            if highest_estimate is None or estimate.estimate > highest_estimate.estimate:
                highest_estimate = estimate

            if lowest_estimate is None or estimate.estimate < lowest_estimate.estimate:
                lowest_estimate = estimate

        if lowest_estimate == highest_estimate:
            return []

        return [lowest_estimate.developer, highest_estimate.developer]
