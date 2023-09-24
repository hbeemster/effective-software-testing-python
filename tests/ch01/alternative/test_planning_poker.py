"""Module to test the alternative implementation of the identify_extremes function."""
from random import shuffle

import pytest
from hypothesis import given, strategies as st

from src.effective_software_testing_python.ch01.alternative.estimate import Estimate
from src.effective_software_testing_python.ch01.alternative.planning_poker import identify_extremes


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
        identify_extremes(value)


# ------------------------------------------------------------------------
def test_two_estimates():

    devs = identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Frank", 5),
        ]
    )

    assert {"Mauricio", "Frank"} == set(devs)


# ------------------------------------------------------------------------
# this test was later deleted by Eleanor, as the property based testing
# replaces this one.
def test_many_estimates():

    devs = identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Arie", 5),
            Estimate("Frank", 7),
        ]
    )

    assert len(devs) == 2
    assert {"Mauricio", "Arie"} == set(devs)


# ------------------------------------------------------------------------
@given(
    estimates=st.lists(
        st.builds(
            Estimate,
            st.text(min_size=1, max_size=5),
            st.integers(2, 99),
        ),
        min_size=1,
        max_size=10,
    )
)
def test_estimates_in_any_order(estimates):
    estimates.append(Estimate("MrLowEstimate", 1))
    estimates.append(Estimate("MsHighEstimate", 100))

    shuffle(estimates)

    devs = identify_extremes(estimates)

    assert {"MrLowEstimate", "MsHighEstimate"} == set(devs)


# ------------------------------------------------------------------------
def test_developers_with_the_same_estimate():
    devs = identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Arie", 5),
            Estimate("Andy", 10),
            Estimate("Frank", 7),
            Estimate("Annibale", 5),
        ]
    )

    # Different result then the book implementation due to the sorting, it is still correct though.
    assert {'Arie', 'Andy'} == set(devs)


# ------------------------------------------------------------------------
def test_all_developers_with_the_same_estimate():
    devs = identify_extremes(
        [
            Estimate("Mauricio", 10),
            Estimate("Arie", 10),
            Estimate("Andy", 10),
            Estimate("Frank", 10),
            Estimate("Annibale", 10),
        ]
    )

    assert [] == devs
