def calculate_degradation(lap_times: list) -> float:
    """
    Estimates tire degradation rate in seconds per lap
    using linear regression slope across a stint.
    Returns: degradation rate (positive = getting slower)
    """
    assert len(lap_times) >= 3, "Minimum 3 laps required"
    assert all(isinstance(t, (int, float)) for t in lap_times), "Lap times must be numbers"
    assert all(t > 0 for t in lap_times), "Lap times must be positive"

    n = len(lap_times)
    x = list(range(n))
    x_mean = sum(x) / n
    y_mean = sum(lap_times) / n

    numerator = sum((x[i] - x_mean) * (lap_times[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    rate = numerator / denominator

    assert -3.0 < rate < 5.0, f"Rate {rate:.3f} outside physical range — check input data"
    return rate