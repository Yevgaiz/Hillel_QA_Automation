import pytest
# import sys
# sys.path.append(r"D:\PycharmProjects\pythonProject\HW_37\..")
# print(sys.path)

from HW_41.pixel.class_pixel import Pixel


class TestPixel:

    def test_pixel_initialization(self):
        p = Pixel(10, 20, 30)
        assert p.red == 10
        assert p.green == 20
        assert p.blue == 30

        with pytest.raises(ValueError):
            Pixel(256, 0, 0)

        with pytest.raises(ValueError):
            Pixel(-1, 0, 0)

    def test_pixel_addition(self):
        p1 = Pixel(0, 1, 255)
        p2 = Pixel(0, 0, 100)
        result = p1 + p2
        assert result.red == 0 and result.green == 1 and result.blue == 255

    def test_pixel_subtraction(self):
        p1 = Pixel(255, 255, 255)
        p2 = Pixel(255, 254, 1)
        result = p1 - p2
        assert result.red == 0 and result.green == 1 and result.blue == 254

        p3 = Pixel(205, 155, 105)
        result = p1 - p3
        assert result.red == 50 and result.green == 100 and result.blue == 150

    def test_pixel_multiplication(self):
        p = Pixel(0.5, 100, 150)
        result = p * 2
        assert result.red == 1 and result.green == 200 and result.blue == 255

        with pytest.raises(TypeError):
            p * "123"

        with pytest.raises(ValueError):
            p * -1

    def test_pixel_division(self):
        p = Pixel(1, 2, 255)
        result = p / 2
        assert result.red == 0.5 and result.green == 1 and result.blue == 127.5

        with pytest.raises(TypeError):
            p / "qqq"

        with pytest.raises(ValueError):
            p / -1

    def test_pixel_equality(self):
        p1 = Pixel(10, 20, 30)
        p2 = Pixel(10, 20, 30)
        p3 = Pixel(20, 30, 40)
        assert p1 == p2
        assert p1 != p3

    def test_pixel_str(self):
        p = Pixel(10, 20, 30)
        expected_str = "Pixel object\n\tRed: 10\n\tGreen: 20\n\tBlue: 30"
        assert str(p) == expected_str

    def test_pixel_repr(self):
        p = Pixel(10, 20, 30)
        assert repr(p) == "Pixel(10, 20, 30)"
