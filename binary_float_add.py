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


def normalize_binary(binary_str, base):
    # Find the position of the first '1' and radix
    first_one_index = binary_str.find("1")
    radix_index = binary_str.find(".")

    if first_one_index == 0 and radix_index == 1:
        return binary_str, base

    # If the first '1' is to the right of the radix point, shift radix to the right
    if first_one_index > radix_index:
        new_exponent = (radix_index - first_one_index) + base
        normalized_str = (
            binary_str[first_one_index] + "." + binary_str[first_one_index + 1 :]
        )
    # If the first '1' is to the left of the radix point, we need to shift radix the left
    else:
        new_exponent = (radix_index - first_one_index - 1) + base
        binary_str = binary_str.replace(".", "")
        normalized_str = (
            binary_str[first_one_index] + "." + binary_str[first_one_index + 1 :]
        )

    return normalized_str, new_exponent


def match_inputs(input1, input2, base1, base2):
    normalized_input1, exp_input1 = normalize_binary(input1, base1)
    normalized_input2, exp_input2 = normalize_binary(input2, base2)

    # remove when done testing
    print("Normalized Input:")
    print(normalized_input1 + " 2^" + str(exp_input1))
    print(normalized_input2 + " 2^" + str(exp_input2) + "\n")

    if exp_input1 > exp_input2:
        normalized_input2 = normalized_input2.replace(".", "")
        normalized_input2 = (
            "0." + ("0" * (exp_input1 - exp_input2 - 1)) + normalized_input2
        )
        exp_input2 = exp_input1

    if exp_input2 > exp_input1:
        normalized_input1 = normalized_input1.replace(".", "")
        normalized_input1 = (
            "0." + ("0" * (exp_input2 - exp_input1 - 1)) + normalized_input1
        )
        exp_input1 = exp_input2

    if len(normalized_input1) == 2:
        normalized_input1 = normalized_input1 + "0"

    if len(normalized_input2) == 2:
        normalized_input2 = normalized_input2 + "0"

    return normalized_input1, normalized_input2, exp_input1, exp_input2


def transform_to_GRS(normalized_binary, numOfBits):
    # Divide the string into the binary and the excess bits
    new_binary = normalized_binary[: numOfBits + 1]
    excess = normalized_binary[numOfBits + 1 :]

    # obtain the G and R portion of GRS and place all the excess bits into a string
    grs = ""

    if len(excess) == 1:
        grs = excess + "00"
    elif len(excess) == 2:
        grs = excess + "0"
    elif len(excess) > 2:
        grs = excess[:2]
        excess = excess[2:]

        # if excess has a 1, then add 1 to the grs, else add 0
        excess = "1" if "1" in excess else "0"
        grs += excess
    else:
        grs = "000"

    return new_binary + grs


def rounding(normalized_binary, numOfBits):
    new_binary = normalized_binary[: numOfBits + 1]
    excess = normalized_binary[numOfBits + 1 :]

    if excess[0] == "0":
        return new_binary
    elif excess[0] == "1" and ("1" in excess[1:] or len(excess) == 1):
        new_binary_list = list(new_binary)
        carry = 1

        for i in range(len(new_binary_list) - 1, -1, -1):
            if new_binary_list[i] == ".":
                continue
            sum_ = int(new_binary_list[i]) + carry
            new_binary_list[i] = str(sum_ % 2)
            carry = sum_ // 2

        if carry:
            new_binary_list.insert(0, "1")

        new_binary = "".join(new_binary_list)

        # Adjust the binary representation to maintain the same number of bits
        if len(new_binary.split(".")[0]) > 1:
            new_binary = new_binary[0] + "." + new_binary[1:]

    elif excess[0] == "1" and all(bit == "0" for bit in excess[1:]):
        new_binary_number = float(new_binary)
        if int(new_binary_number) % 2 == 1:
            last_bit_index = new_binary.rfind("1")
            new_binary_list = list(new_binary)
            carry = 1
            for i in range(last_bit_index, -1, -1):
                if new_binary_list[i] == ".":
                    continue
                sum_ = int(new_binary_list[i]) + carry
                new_binary_list[i] = str(sum_ % 2)
                carry = sum_ // 2
            if carry:
                new_binary_list.insert(0, "1")
            new_binary = "".join(new_binary_list)

        # Adjust the binary representation to maintain the same number of bits
        if len(new_binary.split(".")[0]) > 1:
            new_binary = new_binary[0] + "." + new_binary[1:]

    return new_binary


def binary_addition(num1, num2):
    # Handle negative numbers
    num1_is_negative = num1.startswith('-')
    num2_is_negative = num2.startswith('-')
    
    if num1_is_negative:
        num1 = num1[1:]
    if num2_is_negative:
        num2 = num2[1:]
    
    # Convert the numbers to lists of integers
    int_part1, frac_part1 = num1.split('.')
    int_part2, frac_part2 = num2.split('.')
    
    if num1_is_negative and not num2_is_negative:
        return binary_subtraction(num2, num1)  # Subtract num1 from num2
    elif not num1_is_negative and num2_is_negative:
        return binary_subtraction(num1, num2)  # Subtract num2 from num1
    
    # Pad fractional parts with zeros if needed
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 += '0' * (max_frac_length - len(frac_part1))
    frac_part2 += '0' * (max_frac_length - len(frac_part2))
    
    int_part_sum = bin(int(int_part1, 2) + int(int_part2, 2))[2:]
    
    carry = 0
    frac_part_sum = ''
    for i in range(max_frac_length - 1, -1, -1):
        bit_sum = int(frac_part1[i]) + int(frac_part2[i]) + carry
        frac_part_sum = str(bit_sum % 2) + frac_part_sum
        carry = bit_sum // 2
    
    if carry:
        int_part_sum = bin(int(int_part_sum, 2) + 1)[2:]
    
    result = int_part_sum + '.' + frac_part_sum

    if num1_is_negative and num2_is_negative:
        result = '-' + result
    
    return result


def binary_subtraction(num1, num2):
    flag = False
    if num1 < num2:
        flag = True
        num1, num2 = num2, num1

    int_part1, frac_part1 = num1.split('.')
    int_part2, frac_part2 = num2.split('.')
    
    # Pad fractional parts
    max_frac_length = max(len(frac_part1), len(frac_part2))
    frac_part1 += '0' * (max_frac_length - len(frac_part1))
    frac_part2 += '0' * (max_frac_length - len(frac_part2))
    
    # Perform binary subtraction for fractional parts
    borrow = 0
    frac_part_diff = ''
    for i in range(max_frac_length - 1, -1, -1):
        bit_diff = int(frac_part1[i]) - int(frac_part2[i]) - borrow
        if bit_diff < 0:
            bit_diff += 2
            borrow = 1
        else:
            borrow = 0
        frac_part_diff = str(bit_diff) + frac_part_diff
    
    # Perform binary subtraction for integer parts
    int_part_diff = bin(int(int_part1, 2) - int(int_part2, 2) - borrow)[2:]
    
    result = int_part_diff + '.' + frac_part_diff
    
    # Check if the result is negative
    if flag:
        result = '-' + result
    
    return result


def output_to_text_file(final_answer, base):
    with open("Output.txt", "w") as text_file:
        text_file.write(f"{final_answer} {base}")


def main():
    # string_binary_input1 = get_binary_input()
    # string_binary_input2 = get_binary_input()
    


if __name__ == "__main__":
    main()
