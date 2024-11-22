import math


def area(r):
    """Calculate the area of a circle given its radius."""
    if r <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * r * r


def perimeter(r):
    """Calculate the perimeter (circumference) of a circle given its radius."""
    if r <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * math.pi * r
