# test_square.py
import pytest
import square


class TestSquare:

    def test_area_valid(self):
        """Testing area calculation for a valid square (side 4)."""
        # Arrange
        a = 4

        # Act
        result = square.area(a)

        # Assert
        assert result == 16

    def test_perimeter_valid(self):
        """Testing perimeter calculation for a valid square (side 4)."""
        # Arrange
        a = 4

        # Act
        result = square.perimeter(a)

        # Assert
        assert result == 16

    def test_area_invalid_negative_side(self):
        """Testing area calculation with a negative side (-1)."""
        # Arrange
        a = -1

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            square.area(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_perimeter_invalid_negative_side(self):
        """Testing perimeter calculation with a negative side (-1)."""
        # Arrange
        a = -1

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            square.perimeter(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_area_zero_side(self):
        """Testing area calculation with a zero side (0)."""
        # Arrange
        a = 0

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            square.area(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_perimeter_zero_side(self):
        """Testing perimeter calculation with a zero side (0)."""
        # Arrange
        a = 0

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            square.perimeter(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_square_functions(self):
        """Testing the square functions with various inputs."""
        try:
            side = 4
            print("Area of the square:", square.area(side))
            print("Perimeter of the square:", square.perimeter(side))

            side = -1
            print("Area of the square:", square.area(side))

            side = 0
            print("Perimeter of the square:", square.perimeter(side))

        except ValueError as e:
            print("Error:", e)


TestSquare().test_square_functions()
