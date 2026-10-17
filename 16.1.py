
class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина та висота мають бути більшими за нуль.")

        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        total_square = self.get_square() + other.get_square()
        return Rectangle(total_square, 1)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented

        if n <= 0:
            raise ValueError("Множник має бути більшим за нуль.")

        return Rectangle(self.get_square() * n, 1)

    def __rmul__(self, n):
        return self * n

    def __str__(self):
        return (
            f"Rectangle(width={self.width}, "
            f"height={self.height}, "
            f"square={self.get_square()})"
        )


if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)

    assert r1.get_square() == 8, "Test1"
    assert r2.get_square() == 18, "Test2"

    r3 = r1 + r2
    assert r3.get_square() == 26, "Test3"

    r4 = r1 * 4
    assert r4.get_square() == 32, "Test4"

    assert Rectangle(3, 6) == Rectangle(2, 9), "Test5"

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print("Усі перевірки пройшли успішно!")
