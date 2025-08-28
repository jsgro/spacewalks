import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

def test_text_to_duration_irrational():
    assert text_to_duration("10:20") == pytest.approx(10.33333)
   # assert abs(text_to_duration("10:20") - 10.33333333) < 1e-5

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25



# test_text_to_duration_float()
# test_text_to_duration_integer()
# test_text_to_duration_irrational()

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result