# square.py

def area(a):
    if a <= 0:
        raise ValueError("Side must be positive.")
    return a * a


def perimeter(a):
    if a <= 0:
        raise ValueError("Side must be positive.")
    return 4 * a
