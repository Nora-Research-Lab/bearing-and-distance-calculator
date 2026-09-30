"""
Plain Python logic for bearing and distance calculations.

No Gradio imports are used in this module so it can be tested independently.
"""

import math


EARTH_RADII = {
    "kilometers": 6371.0,
    "miles": 3959.0,
    "nautical_miles": 3440.0,
}

UNIT_DISPLAY = {
    "kilometers": "km",
    "miles": "mi",
    "nautical_miles": "nmi",
}

_UNIT_ALIASES = {
    "kilometers": "kilometers",
    "kilometres": "kilometers",
    "kilometer": "kilometers",
    "kilometre": "kilometers",
    "km": "kilometers",
    "miles": "miles",
    "mile": "miles",
    "mi": "miles",
    "statute_miles": "miles",
    "nautical_miles": "nautical_miles",
    "nautical_mile": "nautical_miles",
    "nautical miles": "nautical_miles",
    "nautical mile": "nautical_miles",
    "nmi": "nautical_miles",
    "nm": "nautical_miles",
}


def _normalize_unit(unit):
    if unit is None:
        raise ValueError("Select a distance unit.")

    key = str(unit).strip().lower().replace("-", "_")
    key = "_".join(key.split())

    if key in _UNIT_ALIASES:
        return _UNIT_ALIASES[key]

    raise ValueError("Unsupported distance unit. Choose kilometers, miles, or nautical miles.")


def _validate_coordinate(value, minimum, maximum, label):
    if value is None:
        raise ValueError(f"{label} is required.")

    try:
        coordinate = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} must be a number.")

    if not math.isfinite(coordinate):
        raise ValueError(f"{label} must be a finite number.")

    if coordinate < minimum or coordinate > maximum:
        raise ValueError(f"{label} must be between {minimum} and {maximum}.")

    return coordinate


def _validate_inputs(lat1, lon1, lat2, lon2):
    lat1 = _validate_coordinate(lat1, -90.0, 90.0, "Point 1 latitude")
    lon1 = _validate_coordinate(lon1, -180.0, 180.0, "Point 1 longitude")
    lat2 = _validate_coordinate(lat2, -90.0, 90.0, "Point 2 latitude")
    lon2 = _validate_coordinate(lon2, -180.0, 180.0, "Point 2 longitude")

    return lat1, lon1, lat2, lon2


def haversine_distance(lat1, lon1, lat2, lon2, unit="kilometers"):
    """
    Calculate great-circle distance using the Haversine formula.

    Returns distance as a float in the selected unit.
    """
    lat1, lon1, lat2, lon2 = _validate_inputs(lat1, lon1, lat2, lon2)
    unit_key = _normalize_unit(unit)

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    lambda1 = math.radians(lon1)
    lambda2 = math.radians(lon2)

    dphi = phi2 - phi1
    dlambda = lambda2 - lambda1

    a = (
        math.sin(dphi / 2.0) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
    )

    a = min(1.0, max(0.0, a))
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    return EARTH_RADII[unit_key] * c


def initial_bearing(lat1, lon1, lat2, lon2):
    """
    Calculate initial bearing from point 1 to point 2.

    Returns bearing in degrees normalized to 0-360.
    """
    lat1, lon1, lat2, lon2 = _validate_inputs(lat1, lon1, lat2, lon2)

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    lambda1 = math.radians(lon1)
    lambda2 = math.radians(lon2)

    dlambda = lambda2 - lambda1

    y = math.sin(dlambda) * math.cos(phi2)
    x = (
        math.cos(phi1) * math.sin(phi2)
        - math.sin(phi1) * math.cos(phi2) * math.cos(dlambda)
    )

    theta = math.atan2(y, x)
    return (math.degrees(theta) + 360.0) % 360.0


def back_bearing(bearing):
    """
    Calculate reciprocal/back bearing from an initial bearing.

    Returns bearing in degrees normalized to 0-360.
    """
    if bearing is None:
        raise ValueError("Bearing is required.")

    try:
        bearing_value = float(bearing)
    except (TypeError, ValueError):
        raise ValueError("Bearing must be a number.")

    if not math.isfinite(bearing_value):
        raise ValueError("Bearing must be a finite number.")

    return (bearing_value + 180.0) % 360.0


def calculate_bearing_and_distance(lat1, lon1, lat2, lon2, unit="kilometers"):
    """
    Calculate distance, initial bearing, and back bearing.

    Returns:
        (distance_float, initial_bearing_float, back_bearing_float)
    """
    distance = haversine_distance(lat1, lon1, lat2, lon2, unit)
    bearing = initial_bearing(lat1, lon1, lat2, lon2)
    reciprocal = back_bearing(bearing)

    return distance, bearing, reciprocal


def calculate_results(lat1, lon1, lat2, lon2, unit="kilometers"):
    """
    Calculate and format the three UI outputs.

    Returns:
        (distance_string, initial_bearing_string, back_bearing_string)
    """
    distance, bearing, reciprocal = calculate_bearing_and_distance(
        lat1, lon1, lat2, lon2, unit
    )

    unit_key = _normalize_unit(unit)
    distance_str = f"{distance:.2f} {UNIT_DISPLAY[unit_key]}"
    bearing_str = f"{bearing:.2f}°"
    reciprocal_str = f"{reciprocal:.2f}°"

    return distance_str, bearing_str, reciprocal_str
