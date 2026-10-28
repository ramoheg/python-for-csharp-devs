from practice_tools.geometry import calculate_rectangle_area
from practice_tools.text import get_word_lengths


def main() -> None:
    width: float = float(input("Width: "))
    height: float = float(input("Height: "))
    area: float = calculate_rectangle_area(width, height)
    print(f"Area: {area}")

    names: list[str] = ["Eva", "Tom", "Jerry", "Marcus", "Joseph"]
    name_lengths: dict[str, int] = get_word_lengths(names)
    print(name_lengths)


if __name__ == "__main__":
    main()