def main() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]

    squared_numbers: list[int] = list(map(lambda x: x ** 2, numbers))

    for number in squared_numbers:
        print(number)


if __name__ == ("__main__"):
    main()
