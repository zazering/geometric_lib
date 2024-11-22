import pytest
from triangle import area, perimeter


class TestTriangle:

    def test_area_valid(self):
        """Testing area calculation for a valid triangle (3, 4, 5)."""
        # Arrange
        a, b, c = 3, 4, 5

        # Act
        result = area(a, b, c)

        # Assert
        assert result == 6.0

    def test_perimeter_valid(self):
        """Testing perimeter calculation for a valid triangle (3, 4, 5)."""
        # Arrange
        a, b, c = 3, 4, 5

        # Act
        result = perimeter(a, b, c)

        # Assert
        assert result == 12

    def test_area_invalid_sides(self):
        """Testing area calculation for a degenerate triangle (1, 2, 3)."""
        # Arrange
        a, b, c = 1, 2, 3

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            area(a, b, c)
        assert str(excinfo.value) == "Sides cannot form a triangle."

    def test_perimeter_invalid_negative_side(self):
        """Testing perimeter calculation with a negative side (-1, 2, 3)."""
        # Arrange
        a, b, c = -1, 2, 3

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            perimeter(a, b, c)
        assert str(excinfo.value) == "Sides cannot form a triangle."

    def test_area_zero_side(self):
        """Testing area calculation with one side equal to zero (0, 2, 3)."""
        # Arrange
        a, b, c = 0, 2, 3

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            area(a, b, c)
        assert str(excinfo.value) == "Sides cannot form a triangle."

    def test_perimeter_zero_side(self):
        """Testing perimeter calculation with one side equal to
        zero (0, 2, 3)."""
        # Arrange
        a, b, c = 0, 2, 3

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            perimeter(a, b, c)
        assert str(excinfo.value) == "Sides cannot form a triangle."

    def test_triangle_functions(self):
        """Test the triangle functions and print results."""
        try:
            side_a = 3
            side_b = 4
            side_c = 5

            print("Triangle area:", area(side_a, side_b, side_c))
            print("Triangle perimeter:", perimeter(side_a, side_b, side_c))

            side_a = 1
            side_b = 2
            side_c = 3

            print("Triangle area:", area(side_a, side_b, side_c))

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    TestTriangle().test_triangle_functions()
