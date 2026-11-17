import pytest
from src.booking_cost import calculate_booking_cost

#TC-BC-01 --> NORMAL
#TC-BC-02 --> CHECK CALCULATIONS
#TC-BC-03 --> CHECK FOR VALUE ERROR
#TC-BC-04--> CHECK FOR TYPE ERROR

@pytest.mark.parametrize(
    "nights,night_rate_cents,expected", [
        (3, 15000, 45000),     # TC-BC-01
        (1, 15000, 15000),     # TC-BC-02
        (30, 15000,45000),   # TC-BC-02
        (5, 0, 0),             # TC-BC-02
    ]
)
def test_valid_cost(nights, night_rate_cents, expected):
    result = calculate_booking_cost(nights, night_rate_cents)
    assert result == expected
    assert type(result) is int



@pytest.mark.parametrize(
    "nights,night_rate_cents", [
        (0, 15000),            # TC-BC-03
        (31, 15000),           # TC-BC-03
        (3, -1),               # TC-BC-03
    ]
)
def test_out_of_range(nights, night_rate_cents):
    with pytest.raises(ValueError):
        calculate_booking_cost(nights, night_rate_cents)



@pytest.mark.parametrize(
    "nights,night_rate_cents", [
        (3.0, 15000),          # TC-BC-04
        ("3", 15000),          # TC-BC-04
        (3, None),             # TC-BC-04
        (True, 15000),         # TC-BC-04
        (3, False),            # TC-BC-04
    ]
)
def test_invalid_type(nights, night_rate_cents):
    with pytest.raises(TypeError):
        calculate_booking_cost(nights, night_rate_cents)