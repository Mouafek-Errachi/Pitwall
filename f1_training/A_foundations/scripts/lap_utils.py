import pandas as pd

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

def clean_mychron_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans MyChron-style column headers into snake_case with unit suffixes.
    Example: 'Speed (km/h)' -> 'speed_kmh'
    """
    unit_map = {
        "km/h": "kmh", "1/min": "rpm_unit",
        "deg": "deg", "c": "c", "s": "s"
    }
    
    def clean_single(col: str) -> str:
        if "(" in col:
            name, unit = col.split("(", 1)
            name = name.strip().lower().replace(" ", "_")
            unit = unit.replace(")", "").strip().lower()
            suffix = unit_map.get(unit, unit.replace("/", ""))
            if suffix == "rpm_unit":
                return name
            return f"{name}_{suffix}" if suffix else name
        return col.strip().lower().replace(" ", "_")
    
    df = df.copy()
    df.columns = [clean_single(c) for c in df.columns]
    return df