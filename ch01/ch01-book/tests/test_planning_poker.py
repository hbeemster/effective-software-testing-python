"""Module to test the PlanningPoker class."""
from ch01_book.esitmate import Estimate
from ch01_book.planning_poker import PlanningPoker
import pytest


# ------------------------------------------------------------------------
@pytest.mark.parametrize(
    "value, expected_message",
    [
        (None, "Estimates can't be None"),
        ([], "There has to be more than 1 estimate in the list"),
        ([Estimate("Eleanor", 1)], "There has to be more than 1 estimate in the list"),
    ],
    ids=[
        "reject_none_input",
        "reject_empty_list",
        "reject_single_estimate",
    ],
)
# ------------------------------------------------------------------------
def test_inputs(value, expected_message):
    with pytest.raises(ValueError, match=expected_message) as e:
        PlanningPoker.identify_extremes(value)


# ------------------------------------------------------------------------
def test_two_estimates():

    devs = PlanningPoker.identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Frank", 5),
        ]
    )

    assert {"Mauricio", "Frank"} == set(devs)


# ------------------------------------------------------------------------
def test_many_estimates():

    devs = PlanningPoker.identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Arie", 5),
            Estimate("Frank", 7),
        ]
    )

    assert {"Mauricio", "Arie"} == set(devs)

# ------------------------------------------------------------------------
def test_all_developers_with_the_same_estimate():
    devs = PlanningPoker.identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Arie", 10),
            Estimate("Andy", 10),
            Estimate("Frank", 10),
            Estimate("Annibale", 10),
        ]
    )

    assert [] == devs
