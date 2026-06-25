import pytest
import lap_utils
def test_normal_degradation():
    # tires getting slower — normal degradation
    laps = [90.1, 90.4, 90.8, 91.2, 91.7]
    rate = lap_utils.calculate_degradation(laps)
    assert rate > 0, f"Expected positive degradation, got {rate:.4f}"
def test_flat_stint():
    # tires holding — near zero degradation
    laps = [90.0, 90.1, 89.9, 90.0, 90.1]
    rate = lap_utils.calculate_degradation(laps)
    assert abs(rate) < 0.2, f"Expected near-zero degradation, got {rate:.4f}"
def test_too_few_laps():
    # should raise an error, not silently return something
    with pytest.raises(AssertionError):
        lap_utils.calculate_degradation([90.0, 90.5])

def test_negative_lap_time():
    # should raise an error, not silently return something
    with pytest.raises(AssertionError):
        lap_utils.calculate_degradation([90.0, -90.5, 91.0])