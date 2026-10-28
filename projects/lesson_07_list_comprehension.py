def main() -> None:
    names: list[str] = ["Eva", "Tom", "Jerry", "Marcus", "Joseph"]

    long_names: list[str] = [name for name in names if len(name) > 5]

    for name in long_names:
        print(name)

if __name__ == "__main__":
    main()