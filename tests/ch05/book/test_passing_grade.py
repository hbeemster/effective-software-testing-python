"""Use Hypothesis for property-based testing.

https://hypothesis.readthedocs.io/en/latest/
"""
import pytest
from hypothesis import given
import hypothesis.strategies as st

from src.effective_software_testing_python.ch05.book.passing_grade import PassingGrade

# ------------------------------------------------------------------------
@given(
    grade=st.floats(min_value=1.0, max_value=5.0, exclude_max=True)

)
def test_fail(grade):
    assert not PassingGrade.passed(grade)

# ------------------------------------------------------------------------
@given(
    grade=st.floats(min_value=5.0, max_value=10.0)

)
def test_pass(grade):
    assert PassingGrade.passed(grade)


# ------------------------------------------------------------------------
@given(
    grade=st.floats().filter(lambda x: x < 1.0 or x > 10.0)
)
def test_invalid(grade):
    with pytest.raises(ValueError):
        PassingGrade.passed(grade)
