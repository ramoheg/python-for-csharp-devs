class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        if length <= 0:
            raise ValueError("Length must be greater than 0.")

        if width <= 0:
            raise ValueError("Width must be greater than 0.")

        self.length: float = length
        self.width: float = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


def main() -> None:
    test_values: list[tuple[float, float]] = [
        (3, 4),
        (10, 7.5),
        (-2, 5),
        (3, 0),
    ]

    for length, width in test_values:
        try:
            rect: Rectangle = Rectangle(length, width)
            print(f"Length: {rect.length}, Width: {rect.width}")
            print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
        except ValueError as e:
            print(f"Error for ({length}, {width}): {e}")

        print()


if __name__ == "__main__":
    main()