def calculate_area(width: float, height: float) -> float:
    # Calculate area of the rectangle
    area: float = width * height

    # Return the result
    return area

def main() -> None:
    print("Welcome to the rectangle calculator!")

    # Ask the user for both sides and convert his input to numbers
    width: float = float(input("Width: "))
    height: float = float(input("Height: "))

    # Calculate the area and print it
    area: float = calculate_area(width, height)
    print(f"Area: {area}")

if __name__ == "__main__":
    main()