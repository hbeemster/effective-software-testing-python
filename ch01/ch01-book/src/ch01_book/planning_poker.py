"""Module with the PlanningPoker class."""
from typing import List, Tuple

from ch01_book.esitmate import Estimate


class PlanningPoker:

    @staticmethod
    def identify_extremes(estimates: List[Estimate] )->Tuple[str, str]:
        """Returns the extremes of the given estimates."""

        if not estimates:
            raise ValueError("Estimates can't be None.");

