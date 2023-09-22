"""Module to test the PlanningPoker class."""
from ch01_book.planning_poker import PlanningPoker
import pytest


def test_reject_none_input():
    with pytest.raises(ValueError, match="Estimates can't be None.") as e:
        PlanningPoker.identify_extremes(None)

