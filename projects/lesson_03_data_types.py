def main() -> None:
    name: str = "Ramon"
    age: int = 17
    numbers: list[int] = [1, 2, 3]
    coordinates: tuple[int, int] = (47, 8)
    ages: dict[str, int] = {"Ramon": 17, "Anna": 22}

    print(f"{name} is {type(name)}")
    print(f"{age} is {type(age)}")
    print(f"{numbers} is {type(numbers)}")
    print(f"{coordinates} is {type(coordinates)}")
    print(f"{ages} is {type(ages)}")


if __name__ == "__main__":
    main()