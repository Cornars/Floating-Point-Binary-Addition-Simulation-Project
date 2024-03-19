def validate_binary(binary):
    parts = binary.split(".")
    if len(parts) > 2:
        return False
    for part in parts:
        for digit in part:
            if digit not in ["0", "1"]:
                return False
    return True


def get_binary_input():
    while True:
        binary = input("Enter a floating-point number in binary format: ")
        if validate_binary(binary):
            return binary
        else:
            print("Invalid binary number. Please try again.")


def main():
    string_binary_input1 = get_binary_input()
    string_binary_input2 = get_binary_input()

    normalized1, exponent1 = normalize_binary(string_binary_input1)
    normalized2, exponent2 = normalize_binary(string_binary_input2)

    print(normalized1, exponent1)
    print(normalized2, exponent2)


if __name__ == "__main__":
    main()
