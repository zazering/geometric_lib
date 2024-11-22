def area(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides cannot form a triangle.")

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides cannot form a triangle.")

    return a + b + c
