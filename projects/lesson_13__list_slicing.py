def main() -> None:
    numbers: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    first_three_numbers: list[int] = numbers[:3]
    last_three_numbers: list[int] = numbers[-3:]
    every_second_number: list[int] = numbers[::2]
    reversed_numbers: list[int] = numbers[::-1]

    print(first_three_numbers)
    print(last_three_numbers)
    print(every_second_number)
    print(reversed_numbers)


if __name__ == "__main__":
    main()