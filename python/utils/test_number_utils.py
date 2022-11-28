import pytest

from python.utils import number_utils


@pytest.mark.parametrize(
    ["dividend", "divisor", "expected"],
    [
        (1, 1, ("1.", "")),
        (1, 2, ("0.5", "")),
        (1, 3, ("0.", "3")),
        (1, 4, ("0.25", "")),
        (1, 6, ("0.1", "6")),
        (1, 7, ("0.", "142857")),
        (1, 11, ("0.", "09")),
        (1, 17, ("0.", "0588235294117647")),
        (1, 117, ("0.", "008547")),
        (1, 600, ("0.001", "6")),
        (1, 700, ("0.00", "142857")),
    ],
)
def test_divide_with_recurring(dividend, divisor, expected):
    result = number_utils.divide_with_recurring(dividend=dividend, divisor=divisor)
    assert expected == result
