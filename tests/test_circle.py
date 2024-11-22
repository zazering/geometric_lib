# test_circle.py
import pytest
import circle


class TestCircle:

    def test_area_valid(self):
        """Testing area calculation for a valid circle (radius 3)."""
        # Arrange
        r = 3

        # Act
        result = circle.area(r)

        # Assert
        assert result == pytest.approx(28.2743, rel=1e-5)

    def test_perimeter_valid(self):
        """Testing perimeter calculation for a valid circle (radius 3)."""
        # Arrange
        r = 3

        # Act
        result = circle.perimeter(r)

        # Assert
        assert result == pytest.approx(18.8496, rel=1e-5)

    def test_area_invalid_negative_radius(self):
        """Testing area calculation with a negative radius (-1)."""
        # Arrange
        r = -1

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            circle.area(r)
        assert str(excinfo.value) == "Radius must be a positive number."

    def test_perimeter_invalid_negative_radius(self):
        """Testing perimeter calculation with a negative radius (-1)."""
        # Arrange
        r = -1

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            circle.perimeter(r)
        assert str(excinfo.value) == "Radius must be a positive number."

    def test_area_zero_radius(self):
        """Testing area calculation with a zero radius (0)."""
        # Arrange
        r = 0

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            circle.area(r)
        assert str(excinfo.value) == "Radius must be a positive number."

    def test_perimeter_zero_radius(self):
        """Testing perimeter calculation with a zero radius (0)."""
        # Arrange
        r = 0

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            circle.perimeter(r)
        assert str(excinfo.value) == "Radius must be a positive number."

    def test_circle_functions(self):
        """Testing the circle functions with various inputs."""
        try:
            radius = 3
            print("Area of the circle:", circle.area(radius))
            print("Perimeter of the circle:", circle.perimeter(radius))

            radius = -1
            print("Area of the circle:", circle.area(radius))

            radius = 0
            print("Perimeter of the circle:", circle.perimeter(radius))

        except ValueError as e:
            print("Error:", e)


TestCircle().test_circle_functions()
