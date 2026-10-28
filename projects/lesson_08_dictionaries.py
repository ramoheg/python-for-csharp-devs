def main() -> None:
    names: list[str] = ["Eva", "Tom", "Jerry", "Marcus", "Joseph"]

    name_length: dict[str, int] = {name: len(name) for name in names}

    print(name_length)

if __name__ == "__main__":
    main()