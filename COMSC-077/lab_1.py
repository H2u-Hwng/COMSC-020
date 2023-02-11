# Huu Hung Nguyen
# 02/11/2023
# lab_1.py
# The program asks the users to enter a number in binary or decimal
# It then asks the users what type  of number it is (binary or decimal)
# It check to make sure the number is legal. If the number is not legal, it
# should error out!
# If the number is legal, convert the number to the other 3 types.

def decimal_to_hexadecimal(decimal):
    """
    Convert decimal to hexadecimal
    """
    hexadecimal = ""
    while (decimal > 0):
        digit = decimal % 16
        if digit > 9:
            hexadecimal = chr(digit + 55) + hexadecimal
        else:
            hexadecimal = str(digit) + hexadecimal

        decimal //= 16

    return hexadecimal


def decimal_to_octal(decimal):
    """
    Convert decimal to octal
    """
    octal = ""
    while (decimal > 0):
        octal = str(decimal % 8) + octal
        decimal //= 8

    return octal


def decimal_to_binary(decimal):
    """
    Convert decimal to binary
    """
    binary = ""
    while (decimal > 0):
        binary = str(decimal % 2) + binary
        decimal //= 2

    return binary


def binary_to_decimal(binary):
    """
    Convert binary to decimal
    """
    decimal = 0
    index = 0
    for digit in binary[::-1]:
        if digit == '1':
            decimal += 2**index
        index += 1

    return decimal


def convert_to_other_types(number, type):
    """
    Convert the number to the other 3 types
    """
    if type == "binary":
        binary = number
        decimal = binary_to_decimal(binary)
    elif type == "decimal":
        decimal = int(number)
        binary = decimal_to_binary(decimal)

    octal = decimal_to_octal(decimal)
    hexadecimal = decimal_to_hexadecimal(decimal)

    return decimal, binary, octal, hexadecimal


def check_valid(number, type):
    """
    Check whether the number is valid
    """
    if type == "binary":
        for digit in number:
            if digit != '0' and digit != '1':
                return False
        return True
    elif type == "decimal":
        for digit in number:
            if ord(digit) < ord('0') or ord(digit) > ord('9'):
                return False
        return True
    else:
        return False


def main():
    """
    Main function that prompts the user for a number and type, and converts it
    to other types
    """
    number = input("Enter a number: ")
    type = input("Is the number binary or decimal? ")

    if (check_valid(number, type)):
        decimal, binary, octal, hexadecimal = convert_to_other_types(
            number, type)
        print(f"\nDecimal = {decimal}\nBinary = {binary}")
        print(f"Octal = {octal}\nHexadecimal = {hexadecimal}")
    else:
        print("\nInvalid number!")


# Call main function
main()
