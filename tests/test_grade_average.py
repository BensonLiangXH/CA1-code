import pytest

from src.grade_average import calculate_average


# Valid marks: range limits, an even sum, and odd sums that must keep the .5 (no rounding down).
@pytest.mark.parametrize("mark_one, mark_two, expected", [
    (0, 0, 0),          # both at the lower limit
    (100, 100, 100),    # both at the upper limit
    (0, 100, 50),       # one at each limit
    (60, 80, 70),       # typical marks, even sum
    (50, 51, 50.5),     # example given in the spec
    (0, 1, 0.5),        # smallest fractional average
    (99, 100, 99.5),    # largest fractional average
])
def test_valid_marks_return_correct_average(mark_one, mark_two, expected):
    # Arrange: marks and expected come from the parametrize table

    # Act
    result = calculate_average(mark_one, mark_two)

    # Assert
    assert result == expected


# Correct type (int) but outside 0-100 -> ValueError (each argument checked separately)
@pytest.mark.parametrize("mark_one, mark_two", [
    (-1, 50),    # mark_one just below the lower limit
    (101, 50),   # mark_one just above the upper limit
    (50, -1),    # mark_two just below the lower limit
    (50, 101),   # mark_two just above the upper limit
])
def test_mark_outside_range_raises_value_error(mark_one, mark_two):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


# Wrong data type -> TypeError (each argument checked separately)
@pytest.mark.parametrize("mark_one, mark_two", [
    ("50", 50),    # mark_one is a string
    (50.0, 50),    # mark_one is a float
    (None, 50),    # mark_one is missing
    (True, 50),    # mark_one is a bool, not a valid int
    (50, "50"),    # mark_two is a string
    (50, 50.0),    # mark_two is a float
    (50, None),    # mark_two is missing
    (50, False),   # mark_two is a bool, not a valid int
])
def test_mark_with_invalid_type_raises_type_error(mark_one, mark_two):
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)