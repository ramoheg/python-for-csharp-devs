def convert_file_to_uppercase(input_path: str, output_path: str) -> None:
    with open(input_path, encoding="utf-8") as source:
        content: str = source.read()

    uppercase_content: str = content.upper()

    with open(output_path, mode="w", encoding="utf-8") as target:
        target.write(uppercase_content)

def main() -> None:
    input_path: str = "resources/input.txt"
    output_path: str = "resources/output.txt"

    convert_file_to_uppercase(input_path, output_path)
    print(f"Converted {input_path} → {output_path}")


if __name__ == "__main__":
    main()