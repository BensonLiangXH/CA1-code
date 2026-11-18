import pytest

from src.grade_pass import has_passed


# Valid scores: boundary values around the pass mark (50) and the range limits (0, 100).
# has_passed() must return the Python bool True or False, so "is" is used instead of "==".
@pytest.mark.parametrize("score, expected", [
    (0, False),     # lowest permitted score
    (49, False),    # just below the pass mark
    (50, True),     # exactly the pass mark (spec: "50 or more is a pass")
    (51, True),     # just above the pass mark
    (100, True),    # highest permitted score
])
def test_valid_score_returns_expected_pass_status(score, expected):
    # Arrange: score and expected come from the parametrize table

    # Act
    result = has_passed(score)

    # Assert
    assert result is expected


def test_valid_score_returns_bool_type():
    # Arrange
    score = 75

    # Act
    result = has_passed(score)

    # Assert
    assert type(result) is bool


# Correct type (int) but outside 0-100 -> ValueError
@pytest.mark.parametrize("score", [
    -1,     # just below the lower limit
    101,    # just above the upper limit
])
def test_score_outside_range_raises_value_error(score):
    with pytest.raises(ValueError):
        has_passed(score)


# Wrong data type -> TypeError
@pytest.mark.parametrize("score", [
    "50",   # string
    50.0,   # float, even though the value is a whole number
    None,   # missing score (spec: None is an invalid type)
    True,   # bool is not a valid int (spec 2.2)
    False,  # bool is not a valid int (spec 2.2)
])
def test_score_with_invalid_type_raises_type_error(score):
    with pytest.raises(TypeError):
        has_passed(score)