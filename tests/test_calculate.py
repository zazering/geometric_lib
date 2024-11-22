import pytest
from calculate import calc


class TestCalculateFunctions:

    def test_calc_circle_area(self):
        """Test for correct calculation of the area of a circle using
        calc."""
        radius = [5]

        result = calc('circle', 'area', radius)

        assert result == pytest.approx(78.53981633974483)

    def test_calc_square_area(self):
        """Test for correct calculation of the area of a square using
        calc."""
        side_length = [4]

        result = calc('square', 'area', side_length)

        assert result == 16

    def test_calc_triangle_area(self):
        """Test for correct calculation of the area of a triangle using
        calc."""
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        result = calc('triangle', 'area', [3, 4, 5])

        assert result == pytest.approx(expected_area)

    def test_calc_triangle_perimeter(self):
        """Test for correct calculation of the perimeter of a triangle using
        calc."""
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c

        result = calc('triangle', 'perimeter', [3, 4, 5])

        assert result == expected_perimeter

    def test_calc_invalid_figure(self):
        """Test for an incorrect figure name."""
        with pytest.raises(AssertionError):
            calc('hexagon', 'area', [5])

    def test_calc_invalid_function(self):
        """Test for an incorrect function name."""
        with pytest.raises(AssertionError):
            calc('circle', 'volume', [5])

    def test_calc_triangle_invalid_sides(self):
        """Test for invalid triangle sides (triangle inequality)."""
        with pytest.raises(ValueError):
            calc('triangle', 'area', [1, 2, 3])
