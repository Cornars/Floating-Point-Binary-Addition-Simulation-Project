def validate_binary(binary):
    parts = binary.split('.')
    if len(parts) > 2:
        return False
    for part in parts:
        for digit in part:
            if digit not in ['0', '1']:
                return False
    return True

def get_binary_input():
    while True:
        binary = input("Enter a floating-point number in binary format: ")
        if validate_binary(binary):
            return binary
        else:
            print("Invalid binary number. Please try again.")

def normalize_binary(binary):
    exponent = 0
    integer_part, fractional_part = binary.split('.')
    
    # Move the binary point to the left until only one digit appears to the left of the binary point
    while len(integer_part) > 1:
        fractional_part = integer_part[-1] + fractional_part
        integer_part = integer_part[:-1]
        exponent += 1
    
    # Move the binary point to the right until only one digit appears to the left of the binary point
    while integer_part == '0' and fractional_part[0] == '0':
        integer_part = fractional_part[0]
        fractional_part = fractional_part[1:]
        exponent -= 1
    
    return f"1.{integer_part}{fractional_part}", exponent
def main():
    string_binary_input1 = get_binary_input()
    string_binary_input2 = get_binary_input()

    normalized1, exponent1 = normalize_binary(string_binary_input1)
    normalized2, exponent2 = normalize_binary(string_binary_input2)

    print(normalized1, exponent1)
    print(normalized2, exponent2)

    

if __name__ == "__main__":
    main()
