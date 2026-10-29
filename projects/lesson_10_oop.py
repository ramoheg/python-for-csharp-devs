class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length: float = length
        self.width: float = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


def main() -> None:
    small: Rectangle = Rectangle(3, 4)
    large: Rectangle = Rectangle(10, 7.5)

    for rect in [small, large]:
        print(f"Length: {rect.length}, Width: {rect.width}")
        print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
        print()


if __name__ == "__main__":
    main()