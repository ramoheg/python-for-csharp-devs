def is_even(number: int) -> bool:
    return number % 2 == 0

def greet_names(names: list[str]) -> None:
    for name in names:
        print(f"Hello {name}")

def sum_up_to(limit: int) -> int:
    total: int = 0
    current: int = 0

    while current < limit:
        current += 1
        total += current

    return total

def main() -> None:
    number: int = int(input("Number: "))

    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    names: list[str] = ["Anna", "Tom", "Joe"]
    greet_names(names)

    sum_up_to_ten: int = sum_up_to(10)
    print(f"Sum up to 10 is {sum_up_to_ten}")

if __name__ == "__main__":
    main()