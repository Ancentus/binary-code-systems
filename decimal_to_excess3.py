def decimal_to_excess3(decimal):
    """
    Convert a decimal number to excess-3 code.
    """

    excess3 = ""
    # Convert the decimal number to a string to make it iterable
    decimal_str = str(decimal)

    # Loop through each digit in the decimal number
    for digit in decimal_str:
        # Add 3 to the digit and convert it back to an integer
        excess3_digit = int(digit) + 3
        # Convert the excess3 digit back to a string and append it to the result
        excess3 += str(excess3_digit)

    # Convert the excess-3 code to binary
    binary_excess3 = "".join(format(int(c), "04b") for c in excess3)
    
    return excess3, binary_excess3

# Take input from the user for the decimal number
decimal_num = int(input("Enter a decimal number: "))
excess3_code, binary_excess3_code = decimal_to_excess3(decimal_num)

print("Decimal Number:", decimal_num)
print("Excess-3 Code:", excess3_code)
print("Binary Excess-3 Code:", binary_excess3_code)