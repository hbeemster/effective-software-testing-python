import pytest

from src.effective_software_testing_python.ch03.book.left_pad_utils import LeftPadUtils


# ------------------------------------------------------------------------
@pytest.mark.parametrize(
    "original_str, size, pad_string, expected_str",
    [
        (None, 10, "-", None),
        ("", 5, "-", "-----"),
        ("abc", -1, "-", "abc"),
        ("abc", 5, None, "  abc"),
        ("abc", 5, "", "  abc"),
        ("abc", 5, "-", "--abc"),
        ("abc", 3, "-", "abc"),
        ("abc", 0, "-", "abc"),
        ("abc", 2, "-", "abc"),
        ("abc", 5, "--", "--abc"),
        ("abc", 5, "---", "--abc"),
        ("abc", 5, "-", "--abc"),
    ],
    ids=[f"T{n}" for n in range(1, 13)],
)
def test_left_pad(original_str, size, pad_string, expected_str):
    assert LeftPadUtils.left_pad(original_str, size, pad_string) == expected_str
