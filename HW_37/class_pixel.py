class Pixel:
    def __init__(self, red, green, blue):
        if not all(0 <= value <= 255 for value in (red, green, blue)):
            raise ValueError("Pixel components must be in the range [0 .. 255].")
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    def __add__(self, other):
        if not isinstance(other, Pixel):
            return NotImplemented
        return Pixel(
            min(self.red + other.red, 255),
            min(self.green + other.green, 255),
            min(self.blue + other.blue, 255)
        )

    def __sub__(self, other):
        if not isinstance(other, Pixel):
            return NotImplemented
        return Pixel(
            max(self.red - other.red, 0),
            max(self.green - other.green, 0),
            max(self.blue - other.blue, 0)
        )

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Multiplier must be an integer or float.")
        if other <= 0:
            raise ValueError("Multiplier must be greater than zero.")
        return Pixel(
            min(int(self.red * other), 255),
            min(int(self.green * other), 255),
            min(int(self.blue * other), 255)
        )

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Multiplicand must be an integer or float.")
        if other <= 0:
            raise ValueError("Multiplicand must be greater than zero.")
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Divisor must be an integer or float.")
        if other <= 0:
            raise ValueError("Divisor must be greater than zero.")
        return Pixel(
            max(int(self.red / other), 0),
            max(int(self.green / other), 0),
            max(int(self.blue / other), 0)
        )

    def __eq__(self, other):
        if not isinstance(other, Pixel):
            return NotImplemented
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __str__(self):
        return f"Pixel object\n\tRed: {self.red}\n\tGreen: {self.green}\n\tBlue: {self.blue}"

    def __repr__(self):
        return f"Pixel({self.red}, {self.green}, {self.blue})"


print(Pixel(0, 1, 2) + Pixel(1, 2, 255))  # Pixel(1, 3, 255)
print(Pixel(10, 20, 30) - Pixel(10, 30, 40))  # Pixel(0, 0, 0)
print(Pixel(1, 10, 100) * 3.5)  # Pixel(3, 35, 255)
print(Pixel(30, 2, 22) / 3)  # Pixel(10, 0, 7)
print(Pixel(1, 2, 3) == Pixel(1, 2, 3))  # True

p = Pixel(1, 2, 3) + Pixel(1, 2, 3)
print(repr(p))
