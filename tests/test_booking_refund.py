from src.booking_refund import is_refundable
import pytest

@pytest.mark.parametrize("hours_before_checkin, flexible_rate",[
    (48,True), #TC-RF-01
    (72,True),


])



def test_flexible_rate_valid(hours_before_checkin,flexible_rate):
    assert is_refundable(hours_before_checkin,flexible_rate) is True


@pytest.mark.parametrize("hours_before_checkin, flexible_rate",[

    (47,True), #TC-RF-2
    (72,False),
    (0,False),
])


def test_flexible_rate_invalid(hours_before_checkin,flexible_rate):
    assert is_refundable(hours_before_checkin,flexible_rate) is False



@pytest.mark.parametrize("hours_before_checkin, flexible_rate",[

    (-1,True), #TC-RF-3
  
])


def test_negative_hours_before_checkin(hours_before_checkin,flexible_rate):
    with pytest.raises(ValueError):
        is_refundable(hours_before_checkin,flexible_rate)



@pytest.mark.parametrize("hours_before_checkin, flexible_rate",[
 (48.0, True), #TC-RF-4
 ("48", True),
 (True, True),
 (48, 1),
 (48, "True"),

])


def test_invalid_types_hours_before_checkin(hours_before_checkin,flexible_rate):
    with pytest.raises(TypeError):
                is_refundable(hours_before_checkin,flexible_rate)