# Huu Hung Nguyen
# 02/19/2023
# lab_2.py
# The program asks the users to enter a number in decimal and converts a
# floating point number to the simple model of the floating point
# representation. The simple model uses 1 bit for sign, 5 bits for exponents
# and 8 bits for significand.

def right_part(num):
    index = num.index(".")
    right = num[index + 1:]
    return right


def significand(dec_number):
    significand = left_part(dec_number) + right_part(dec_number)
    first_eight_bits = significand[:8]
    return first_eight_bits


def left_part(binary):
    index = binary.index(".")
    left = binary[:index]
    return left


def exponent(num):
    binary_power = decimal_to_binary(len(left_part(num)))
    index = binary_power.index(".")
    left = binary_power[:index]
    zeros_length = 5 - len(left)
    for i in range(zeros_length):
        left = "0" + left
    return left


def sign_bit(dec_number):
    if dec_number < 0:
        return "1"
    return "0"


def decimal_to_binary(num):
    """
    Convert decimal to binary
    """
    binary = ""
    integer = int(num)
    fractional = num - integer

    # Integer part
    while integer > 0:
        reminder = integer % 2
        binary = str(reminder) + binary
        integer //= 2

    binary += "."

    # Fractional part
    for _ in range(8):
        fractional *= 2
        fract_bit = int(fractional)
        if fract_bit == 1:
            fractional -= fract_bit
            binary += "1"
        else:
            binary += "0"

    return binary


def main():
    """
    Main function that converts a floating point number to the simple model of
    the floating point representation
    """
    num = float(input("Enter a number: "))
    binary = decimal_to_binary(abs(num))
    print(binary)
    print(sign_bit(num) + "-" + exponent(binary) + "-" + significand(binary))


# Call main function
if __name__ == "__main__":
    main()