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

def binary_addition(num1, num2):
    # Convert the numbers to lists of integers
    int_part1, frac_part1 = num1.split('.')
    int_part2, frac_part2 = num2.split('.')
    
    int_part_sum = bin(int(int_part1, 2) + int(int_part2, 2))[2:]
    
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 += '0' * (max_frac_length - len(frac_part1))
    frac_part2 += '0' * (max_frac_length - len(frac_part2))
    
    carry = 0
    frac_part_sum = ''
    for i in range(max_frac_length - 1, -1, -1):
        bit_sum = int(frac_part1[i]) + int(frac_part2[i]) + carry
        frac_part_sum = str(bit_sum % 2) + frac_part_sum
        carry = bit_sum // 2
    
    if carry:
        int_part_sum = bin(int(int_part_sum, 2) + 1)[2:]
    
    result = int_part_sum + '.' + frac_part_sum
    return result

def main():
    string_binary_input1 = get_binary_input()
    string_binary_input2 = get_binary_input()


if __name__ == "__main__":
    main()
