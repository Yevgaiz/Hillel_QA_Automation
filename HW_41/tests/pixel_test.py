import pytest
# import sys
# sys.path.append(r"D:\PycharmProjects\pythonProject\HW_37\..")
# print(sys.path)

from HW_41.pixel.class_pixel import Pixel


class TestPixel:
    @pytest.mark.parametrize("red,green,blue", [
        (10, 20, 30),
        (0, 0, 0),
        (255, 255, 255)
    ])
    def test_pixel_initialization(self, red, green, blue):
        p = Pixel(red, green, blue)
        assert p.red == red
        assert p.green == green
        assert p.blue == blue

    @pytest.mark.parametrize("red,green,blue", [
        (256, 0, 0),
        (-1, 0, 0),
        (0, 256, 0),
        (0, -1, 0),
        (0, 0, 256),
        (0, 0, -1)
    ])
    def test_pixel_initialization_invalid(self, red, green, blue):
        with pytest.raises(ValueError):
            Pixel(red, green, blue)

    @pytest.mark.parametrize("p1, p2, expected", [
        (Pixel(100, 150, 200), Pixel(100, 100, 100), Pixel(200, 250, 255)),
        (Pixel(10, 20, 30), Pixel(20, 30, 40), Pixel(30, 50, 70)),
        (Pixel(200, 200, 200), Pixel(200, 200, 200), Pixel(255, 255, 255))
    ])
    def test_pixel_addition(self, p1, p2, expected):
        result = p1 + p2
        assert result == expected

    @pytest.mark.parametrize("p1, p2, expected", [
        (Pixel(100, 150, 200), Pixel(50, 100, 150), Pixel(50, 50, 50))
    ])
    def test_pixel_subtraction_nominal(self, p1, p2, expected):
        result = p1 - p2
        assert result == expected

    @pytest.mark.parametrize("p1, p2, expected", [
        (Pixel(100, 150, 200), Pixel(100, 100, 100), Pixel(0, 50, 100)),
        (Pixel(0, 150, 200), Pixel(100, 100, 100), Pixel(0, 50, 100)),
        (Pixel(100, 0, 200), Pixel(100, 100, 100), Pixel(0, 0, 100)),
        (Pixel(100, 150, 0), Pixel(100, 100, 100), Pixel(0, 50, 0)),

    ])
    def test_pixel_subtraction_result_zero(self, p1, p2, expected):
        result = p1 - p2
        assert result == expected

    @pytest.mark.parametrize("p1, p2, expected", [
        (Pixel(100, 50, 25), Pixel(150, 75, 50), Pixel(0, 0, 0)),
        (Pixel(50, 100, 200), Pixel(100, 150, 250), Pixel(0, 0, 0))
    ])
    def test_pixel_subtraction_result_below_zero(self, p1, p2, expected):
        result = p1 - p2
        assert result == expected

    @pytest.mark.parametrize("pixel, multiplier, expected", [
        (Pixel(50, 100, 150), 2, Pixel(100, 200, 255)),
        (Pixel(10, 20, 30), 3.5, Pixel(35, 70, 105))
    ])
    def test_pixel_multiplication(self, pixel, multiplier, expected):
        result = pixel * multiplier
        assert result == expected

    @pytest.mark.parametrize("pixel, multiplier", [
        (Pixel(50, 100, 150), "123"),
        (Pixel(50, 100, 150), -1)
    ])
    def test_pixel_multiplication_invalid(self, pixel, multiplier):
        with pytest.raises((TypeError, ValueError)):
            pixel * multiplier

    @pytest.mark.parametrize("pixel, divisor, expected", [
        (Pixel(50, 100, 150), 2, Pixel(25, 50, 75)),
        (Pixel(30, 60, 90), 3, Pixel(10, 20, 30)),
        (Pixel(25, 35, 155), 2, Pixel(12.5, 17.5, 77.5)),
    ])
    def test_pixel_division(self, pixel, divisor, expected):
        result = pixel / divisor
        assert result == expected

    @pytest.mark.parametrize("pixel, divisor", [
        (Pixel(50, 100, 150), "123"),
        (Pixel(50, 100, 150), -1)
    ])
    def test_pixel_division_invalid(self, pixel, divisor):
        with pytest.raises((TypeError, ValueError)):
            pixel / divisor

    @pytest.mark.parametrize("p1, p2, expected", [
        (Pixel(10, 20, 30), Pixel(10, 20, 30), True),
        (Pixel(10, 20, 30), Pixel(20, 30, 40), False)
    ])
    def test_pixel_equality(self, p1, p2, expected):
        assert (p1 == p2) == expected

    @pytest.mark.parametrize("pixel, expected_str", [
        (Pixel(10, 20, 30), "Pixel object\n\tRed: 10\n\tGreen: 20\n\tBlue: 30")
    ])
    def test_pixel_str(self, pixel, expected_str):
        assert str(pixel) == expected_str

    @pytest.mark.parametrize("pixel, expected_repr", [
        (Pixel(10, 20, 30), "Pixel(10, 20, 30)")
    ])
    def test_pixel_repr(self, pixel, expected_repr):
        assert repr(pixel) == expected_repr
